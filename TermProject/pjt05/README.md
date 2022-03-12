# PJT 05

## 프레임워크 기반 웹 페이지 구현

1. 목표 
   - 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
   - Django web framework를 통한 데이터 조작
   - ORM(Object Relational Mapping)에 대한 이해
   - 관리자 페이지를 통한 데이터 관리



이번 실습은 이번주에 진행했던 Django 기반 웹 페이지 구현 수업과 비슷한 부분이 많아 다른 실습에 비해 덜 고생했다!! 교수님과 같이 여러번 반복해서 페이지를 만들다 보니 조금 익숙해진 것도 있는 것 같다.

전체적인 틀은 어제 Workshop과 내용이 비슷했다.

먼저 가상환경에서 django 프로젝트와 앱을 생성했다. settings.py에 앱 이름을 넣어주는 것도 잊지 않았다.

그 후 모델 클래스를 정의하여 여러개의 영화 정보를 담을 수 있도록 해주었다. 파이썬 객체 지향 수업 때는 와닿지 않았는데, django를 배우면서 클래스에 대해 잘 알게 되는 것 같다. 모델 정의 후에 admin.py에서 admin site에 등록할 수 있도록 설정해주었다.

`/movies/` 경로일 때 앱 내 urls.py로 관리할 수 있도록 경로를 추가했고, 그 후 기본 페이지인 base.html을 기반으로 urls.py > views.py > indx.html 순으로 기본 페이지를 구성했다.

![image-20220311152638092](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220311152638092.png)

영화 제목과 평점을 표시했고, 제목을 클릭하면 상세 조회 페이지인 detail.html을 표시하도록 해주었다.

views.py의 detail 함수의 경우 Movie 클래스 내에서 선택한 영화의 정보를 가져와야 하기 때문에 pk를 이용했다.

```python
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    context ={
        'movie' : movie
    }

    return render(request, 'movies/detail.html', context)
```



![image-20220311153314009](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220311153314009.png)

New 버튼을 누르면 새로운 영화를 작성하는 new.html 페이지로 이동했다.

new.html 과 create 함수를 연동하여 Movie 클래스에 입력값을 받아 저장해주었다.

```python
def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie = Movie()
    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()

    return redirect('movies:index')
```

```html
<form action="{% url 'movies:create' %}" method="POST">
  {% csrf_token %}
  <div>
    <label for="title">TITLE</label>
    <input type="text" id='title' name='title'>
  </div>
  <div>
    <label for="audience">AUDIENCE</label>
    <input type="text" id='audience' name='audience'>
  </div>
  <div>
    <label for="release_date">RELEASE_DATE</label>
    <input type="date" id='release_date' name='release_date'>
  </div>
  <div>
    <label for="genre">GENRE</label>
    <select name="genre" id="genre">
      <option value="코미디">코미디</option>
      <option value="드라마">드라마</option>
      <option value="SF">SF</option>
      <option value="공포">공포</option>
    </select>
  </div>
  <div>
    <label for="score">SCORE</label>
    <input type="text" id='score' name='score'>
  </div>
  <div>
    <label for="poster_url">POSTER_URL</label>
    <input type="text" id='poster_url' name='poster_url'>
  </div>
  <div>
    <label for="description">DESCRIPTION</label>
    <input type="text" name="description" id="description">
  </div>
  <button>Submit</button>
  <hr>
  <a href="{% url 'movies:index' %}">BACK</a>

</form>
```



그런데 이렇게 했더니 정보를 입력하지 않거나 audience, score 같은 int 형식의 input에 글자를 작성하는 경우 오류가 발생했다.

![image-20220311154019995](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220311154019995.png)

이런 오류를 예외처리해주고 싶어 구글링도 해보았지만, 이해할 수 없는 내용이었다. 결국 교수님께 도움을 요청했고, 교수님께서는 다음 수업 때 이 내용에 대해 다룬다고 말씀해주시며 현재 할 수 있는 방법은 if문을 활용한 예외처리 방법이 최선이라고 말씀해주시고 아이디어를 제공해주셨다.

아이디어는 어렵지 않았다. html을 통해 사용자에게서 받아온 input 값이 형식에 맞지 않으면 error페이지를 표시하는 방법이었다.

먼저 views.py의 create 함수에서 조건문으로 에러를 감지해 error라는 딕셔너리에 저장한다. 그 후 에러 메세지를 '**context에 담아서**'(이 부분이 중요해보였다. context로 일정하게 넘기지 않으면 처리하기 힘들었다.) html로 넘겨주었다.

```python
errors = {
        'title' : '',
        'audience' : '',
        'score' : '',
        'date' : '',

    }

    if not title:
        errors['title'] = 'Title을 정확히 입력하세요!'
        context = {
            'errors' : errors
        }
        return render(request, 'movies/errors.html', context)

    if not audience.isdigit():
        errors['audience'] = 'Audience를 정확히 입력하세요! (audience에는 숫자만 입력해야 합니다.)'
        context = {
            'errors' : errors
        }
        return render(request, 'movies/errors.html', context)

    if not score.isdigit():
        errors['score'] = 'Score를 정확히 입력하세요! (score에는 숫자만 입력해야 합니다.)'
        context = {
            'errors' : errors
        }
        return render(request, 'movies/errors.html', context)

    if not release_date:
        errors['date'] = 'Release date를 정확히 입력하세요!'
        context = {
            'errors' : errors
        }
        return render(request, 'movies/errors.html', context)
```

그 후 errors.html에서 이를 받아 조건문에 따른 글씨를 보여주도록 했다.

```html
{% extends 'base.html' %}

{% block content %}

{% if errors.title  %}

<p>{{ errors.title }}</p>

{% endif %}

{% if errors.audience %}

<p>{{ errors.audience }}</p>

{% endif %}

{% if errors.score %}

<p>{{ errors.score }}</p>

{% endif %}

{% if errors.date %}

<p>{{ errors.date }}</p>

{% endif %}

{% endblock content %}
```

이런 식으로 설정했더니 에러페이지로 정상적으로 넘어가는 것을 확인할 수 있었다.

![image-20220311155228765](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220311155228765.png)

edit 함수도 create 함수와 거의 유사했다. value값을 지정해서 초기 값을 정해주는 것을 제외하면 코드가 거의 유사했다. 여기서도 마찬가지로 예외처리를 해주었다.



오늘 실습을 통해 django의 기본 흐름에 대해 다시 한번 다질 수 있어서 정말 좋은 시간이었다. 다음에 배우게 될 회원가입, 로그인 등의 기능들도 빨리 배워보고 싶다.

