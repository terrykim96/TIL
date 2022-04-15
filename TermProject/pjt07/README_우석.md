# PJT 07



## 사용자 인증기반 관계형 DB 설계 (페어 프로그래밍을 곁들인,,)

1. 목표  

   - 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작

   - Django web framework를 통한 데이터 조작

   - ORM(Object Relational Mapping)에 대한 이해

   - Django Authentication System에 대한 이해

   - Database many to one relationship(1:N)에 대한 이해

     +) 페어 프로그래밍의 이해

     



## 1. AUTH_USER_MODEL

### settings.py

``` python
AUTH_USER_MODEL = 'accounts.User'
```

### accounts/forms.py

```python
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
```

### accounts/views.py

```python
def signup(request):
    """
    - GET: 회원가입 폼이 담긴 페이지 응답
    - POST: 사용자 회원정보 받아서 회원가입
    """
    if request.user.is_authenticated:
        return redirect('movies:index')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.add_message(request, messages.INFO, '가입이 완료되었습니다')
            return redirect('movies:index')

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)
```

### accounts/admin.py

```python
admin.site.register(User)
```

### accounts/models.py

```python
class User(AbstractUser):
    pass
```

- 먼저 AUTH_USER_MODEL을 활용해 AbstractUser 모델 클래스를 사용했습니다.

  처음에 그냥 get_user_model을 사용해 사용하다가 db를 다 날리고 다시 해야했습니다..

  제일 먼저 accounts/models.py에  AbstractUser를 상속받는 User 클래스를 추가해준 뒤 settings.py에 AUTH_USER_MODEL = 'accounts.User' 를 추가하고 accounts/admin.py에 admin.site.register(User)도 추가해 주었습니다.

  이렇게 했더니 UserCreationForm을 이용할 때 필드의 이름이 달라 오류가 발생해 CustomUserCreationForm을 생성하여 사용자 정보를 넘겨주어야 했습니다. 



### movies/models.py

```python
from django.db import models
from pjt07.settings import AUTH_USER_MODEL

class Movie(models.Model):
    title = models.CharField(max_length=20)
    poster_url = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(
        AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )

class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(
        Movie, 
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
    )
```

- 또한 Movie 클래스에 FK를 적용할 때도 User가 아닌 AUTH_USER_MODEL을 사용했습니다.





## 2. comments_create & user

### movies/views.py

```python
def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comments = comment_form.save(commit=False)
            comments.save()

            return redirect('movies:detail', movie.pk)
    else:
        comment_form = CommentForm()

    comments = movie.comment_set.all()

    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments' : comments,
    }
    return render(request, 'movies/detail.html', context)
  
...

@login_required
@require_POST
def comments_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()

    return redirect('movies:detail', movie.pk)
```

- comments를 구현할 때, 처음에 object()를 이용하여 가져왔더니, 각 게시글에 해당하는 댓글이 아닌 모든 게시글의 댓글을 가져오는 참사(..!)가 일어났습니다. 이를 해결하기 위해 comment_set.all()을 이용하여 pk 값을 받아 각 게시글에 해당하는 댓글만 가져오도록 했습니다.
- 댓글에 request.user를 가져와 comment에 저장하고 detail 함수에서 detail.html 에 comment에 user name를 전달해서 댓글옆에 작성자의 이름도 같이 출력할 수 있게 해주었습니다. 

### 구현하고 싶었던 기능

- 기능 구현 자체는 일찍 끝나서 교수님께서 추가 도전 과제를 주셨습니다. 대댓글을 구현하는 것이었는데,  교수님께서 힌트를 주신 것은 재귀적으로 자기 자신을 FK로 가진 필드를 만들면 된다고 하셨습니다.

  ``` python
  class Comment(models.Model):
      content = models.CharField(max_length=100)
      movie = models.ForeignKey(
          Movie, 
          on_delete=models.CASCADE,
      )
      user = models.ForeignKey(
          AUTH_USER_MODEL, 
          on_delete=models.CASCADE,
      )
      parent = models.ForeignKey(
          'self',
          on_delete=CASCADE,
          null = True
      )
  ```

  이렇게 ForeignKey를 `'self'`로 지정해 주어서 자기 자신을 참조할 수 있도록 해주는 데까지는 성공했습니다. 하지만 그 이후 detail 함수와 html에서의 구현은 어떻게 해야할지 몰라 하지 못했습니다. 더 알아본 뒤 이후에 추가로 구현해보고 싶습니다.



- 그리고 댓글 창의 크기를 조절하고 싶었습니다. 구글링을 해보니 forms.py에서 widget=attrs{'size'}를 통해 설정하라고 했지만 실제로 적용되지 않아 애를 먹다가 시간이 지나 실패했습니다. 댓글 창의 크기가 너무 작은 것을 수정하고 싶었지만 할 수 없었습니다.

  

## Project Review

- 오늘은 페어 프로그래밍을 해보면서  사용자 인증 기반 관계형 DB를 설계해 보았습니다.

  페어님의 은총(갓재호,,)에 힘입어 전에 구현해보지 못했던 기능들도 많이 구현할 수 있었습니다. (검색, pagination 등..) 제가 인터넷 연결이 원활하지 못했던 바람에 끊김이 있어 시간이 부족해 새로운 기능을 구현하지는 못했지만, 그래도 서로 navigator와 driver를 번갈아가며 수행하면서 프론트와 백의 협업을 간접 경험할 수 있어 좋았습니다. 









