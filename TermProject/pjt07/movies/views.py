from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator


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

@login_required
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()

            messages.add_message(request, messages.INFO, '글이 작성되었습니다')
            return redirect('movies:index')
    else:
        form = MovieForm()

    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


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


def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, '글이 수정되었습니다')
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)

    context = {
        'form': form,
    }
    return render(request, 'movies/update.html', context)


def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        messages.add_message(request, messages.INFO, '글이 삭제되었습니다')
        return redirect('movies:index')
    return redirect('movies:detail', movie.pk)


def search(request):
    movies = Movie.objects.all()
    search_key = request.GET.get('search_key')
    movies = movies.filter(title__icontains=search_key)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/search.html', context)


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


@login_required
@require_POST
def comments_delete(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)
