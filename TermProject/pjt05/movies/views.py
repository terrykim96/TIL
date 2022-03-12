from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.

def index(request):
    movie_list = Movie.objects.order_by('title')

    context ={
        'movie_list' : movie_list
    }

    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    context ={
        'movie' : movie
    }

    return render(request, 'movies/detail.html', context)

def new(request):
    return render(request, 'movies/new.html')

def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    context = {
        'movie' : movie
    }

    return render(request, 'movies/edit.html', context)

def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

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

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    movie.delete()

    return redirect('movies:index')

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    new_title = request.POST.get('title')
    new_audience = request.POST.get('audience')
    new_release_date = request.POST.get('release_date')
    new_genre = request.POST.get('genre')
    new_score = request.POST.get('score')
    new_poster_url = request.POST.get('poster_url')
    new_description = request.POST.get('description')

    errors = {
        'title' : '',
        'audience' : '',
        'score' : '',
        'date' : '',

    }

    if not new_title:
        errors['title'] = 'Title을 정확히 입력하세요!'
        context = {
            'errors' : errors
        }
        return render(request, 'movies/errors.html', context)

    if not new_audience.isdigit():
        errors['audience'] = 'Audience를 정확히 입력하세요! (audience에는 숫자만 입력해야 합니다.)'
        context = {
            'errors' : errors
        }
        return render(request, 'movies/errors.html', context)

    if not new_score.isdigit():
        errors['score'] = 'Score를 정확히 입력하세요! (score에는 숫자만 입력해야 합니다.)'
        context = {
            'errors' : errors
        }
        return render(request, 'movies/errors.html', context)

    if not new_release_date:
        errors['date'] = 'Release date를 정확히 입력하세요!'
        context = {
            'errors' : errors
        }
        return render(request, 'movies/errors.html', context)

    movie.title = new_title
    movie.audience = new_audience
    movie.release_date = new_release_date
    movie.genre = new_genre
    movie.score = new_score
    movie.poster_url = new_poster_url
    movie.description = new_description
    movie.save()

    return redirect('movies:detail', movie.pk)
