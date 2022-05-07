# PJT 09



## 알고리즘을 적용한 서버 구성

1.  목표

   - 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web Application 제작  
   - AJAX 통신과 JSON 구조에 대한 이해  
   - Database 1:N, M:N 관계의 이해와 데이터 관계 설정 
   - 영화 추천 알고리즘 설계
   




## 1. Movies 앱 구성

### movies/models.py

``` python
from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

```

- 주어진 스켈레톤 코드에서 영화 추천 알고리즘을 구현하기 위해 영화마다 좋아요 기능을 추가해주었습니다. Movie 클래스에 `like_users`로 User와 M:N 관계를 설정해주었습니다. 각 영화마다 좋아하는 user 정보를 저장하고, 양쪽 모두에서 table에 접근할 수 있습니다.

  

### movies/views.py

```python
from django.shortcuts import redirect, render, get_object_or_404
from .models import Movie, Genre
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_safe
from django.core.paginator import Paginator

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_ln = paginator.page_range

    context = {
        'page_obj': page_obj,
        'movies': movies,
        'page_ln': page_ln,
        'last': page_ln[-1],
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    user = request.user
    my_movies = Movie.objects.filter(like_users=user.pk)
    user_list = []
    for my_movie in my_movies:
        now_users = my_movie.like_users.all()
        for now_user in now_users:
            if now_user not in user_list:
                user_list.append(now_user)
    user_list.remove(user)
    
    recommended_movies = []
    for movie_like_user in user_list:
        now_movies = Movie.objects.filter(like_users=movie_like_user.pk)
        for now_movie in now_movies:
            if now_movie not in recommended_movies:
                recommended_movies.append(now_movie)
    for my_movie in my_movies:
        if my_movie in recommended_movies:
            recommended_movies.remove(my_movie)

    recommended_movies.sort(key=lambda x : -x.vote_average)
    recommended_movies = recommended_movies[:10]
    add_movies = Movie.objects.order_by('-vote_average')[:10]
    
    for add_movie in add_movies:
        if len(recommended_movies) >= 10:
            break
        if add_movie not in recommended_movies:
            recommended_movies.append(add_movie)
        
    paginator = Paginator(recommended_movies, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_ln = paginator.page_range

    context = {
        'page_obj': page_obj,
        'recommended_movies': recommended_movies,
        'page_ln': page_ln,
        'last': page_ln[-1],
    }
    return render(request, 'movies/recommended.html', context)


@require_POST
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
        else:
            movie.like_users.add(user)
        return redirect('movies:detail', movie_pk)
    return redirect('accounts:login')
```

- 명세서에 맞게 `index, detail` 함수를 구현했습니다. 이 때, pagination을 이용해 한 페이지에 5개씩 표시하도록 해주었습니다.
- `like`함수로 user가 좋아하는 영화를 저장해줍니다.
- 영화 추천 알고리즘은 협업 필터링(collaborative filtering)을 참고한 알고리즘을 사용했습니다. 
  1. 먼저 사용자가 '좋아요'를 누를 영화에 접근합니다.
  2. 그 영화에 '좋아요'를 누른 다른 사용자의 정보에 접근합니다.
  3. 다른 사용자가 '좋아요'를 누른 영화들 중 평점이 높은 영화들을 추천합니다.
- 이를 바탕으로 `recommended` 함수를 작성했습니다.








## Project Review

- 오늘은 페어 프로그래밍으로 영화 추천 알고리즘을 구현해 보았습니다.

  git branch를 이용해 협업하면서 동시에 다른 코드를 작성할 수 있어 좋았습니다. 잘 안되는 부분을 함께 고민하면서 헤쳐나가는 좋은 경험을 할 수 있었던 것 같습니다. 초기에 구현하고자 목표했던 기능들을 거의 다 구현하는 데에 성공한 것 같아 성취감이 크게 느껴지는 프로젝트였습니다.









