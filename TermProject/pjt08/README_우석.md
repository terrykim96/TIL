# PJT 08



## DB 설계를 활용한 REST API 설계

1.  목표

   - DRF(Django Rest Framework)를 활용한 API Server 제작
   
   - Database 1:N, M:N에 대한 이해
     
   




## 1. Model / Serializers 설정

### movies/models.py

``` python
from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(
        Actor
    )


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
```

### movies/serializers.py

```python
from rest_framework import serializers
from .models import Actor, Movie, Review


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview')


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name')


class ActorSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
      
        class Meta:
            model = Movie
            fields = ('title', )

    movie_set = MovieTitleSerializer(read_only=True, many=True)

    class Meta:
        model = Actor
        fields = ('id', 'movie_set', 'name')


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content')


class MovieSerializer(serializers.ModelSerializer):
    class ActorNameSerializer(serializers.ModelSerializer):
      
        class Meta:
            model = Actor
            fields = ('name', )

    actors = ActorNameSerializer(read_only=True, many=True)
    review_set = ReviewListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path')

class ReviewSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
      
        class Meta:
            model = Movie
            fields = ('title', )

    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content')
```

- 먼저 명세서에 나온대로 Models.py를 작성했습니다. json파일을 불러오기 위해 변수명을 맞춰줘야하는 것이 번거로웠지만, 오류 내용에 써져있어서 다행히 찾을 수 있었습니다.

  그 후 serializers.py를 작성했는데 여기서 많은 어려움이 있었습니다.. M:N 관계의 경우 서로 상대의 필드를 참조하기 때문에 모델 내부에서 변수명을 정할 때, 상대의 필드명을 사용해주어야 참조할 수 있습니다. 이것을 완화하기 위해 related_name을 사용할 수 있다고 합니다. 여기서 1시간 가량을 소비했던 것 같습니다..

  참조한 필드가 불러와지지 않아 계속 고생을 했는데 다행히 페어 희철님의 도움으로 잘 해결할 수 있었습니다.





## 2. Urls / Views 설정

### movies/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:pk>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:pk>/reviews/', views.create_review),
    path('movies/<int:pk>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:pk>/', views.review_detail),
]
```

- urls.py에는 명세서와 같은 url로 작성해주었습니다. 여기서 `views.create_review`와 `views.movie_detail` 의 순서를 잘 맞춰주어야 합니다. 'movies/< int:pk>/'가 먼저 오면 뒤의 reviews/를 받기 전에 views.movie_detail로 진입해버리기 때문입니다.



### movies/views.py

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Actor, Movie, Review
from .serializers import(
    ActorListSerializer,
    ActorSerializer,
    MovieListSerializer,
    MovieSerializer,
    ReviewListSerializer,
    ReviewSerializer
)
from movies import serializers


@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)

    serializer = ActorSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'GET':
        serializers = ReviewSerializer(review)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = ReviewSerializer(data=request.data, instance=review)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'id' : f'{pk}'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = ReviewListSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
```

- 명세서에 맞게 기능을 views.py에서 구현했습니다. 이번주에 수업했던 내용들과 유사한 내용들이 많아서 그리 어렵지 않게 구현할 수 있었습니다. 다만 댓글을 생성하는 부분에서 변수명을 일치시키지 않으면 save함수가 작동하지 않았습니다.



### 구현하고 싶었던 기능

- 이번 과제는 생각보다 오래걸리고 고생도 많이 했습니다. 그래서 구현하고싶은 추가 과제에 대해 생각해보지 못했던 것 같습니다. 그래도 이후에 저번 프로젝트 때 하지 못했던 대댓글 기능을 api와 serializer를 통해 구현해보아도 재밌겠다는 생각을 했습니다.




## Project Review

- 오늘은 페어 프로그래밍을 해보면서  DB설계를 활용하여 Rest API를 설계해 보았습니다.

  서로 navigator와 driver를 번갈아가며 수행하면서 프론트와 백의 협업을 간접 경험할 수 있어 좋았습니다. 잘 안되는 부분을 함께 고민하면서 헤쳐나가는 좋은 경험을 할 수 있었던 것 같습니다.









