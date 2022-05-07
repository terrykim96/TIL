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