from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie
from django.contrib import messages
from .forms import MovieForm

# Create your views here.
def index(request):
    movie_list = Movie.objects.order_by('title')

    context ={
        'movie_list' : movie_list
    }

    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    context = {
        'movie' : movie
    }

    return render(request, 'movies/detail.html', context)

def create(request):

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '글이 성공적으로 작성되었습니다.',fail_silently=True,)
            return redirect('movies:index')
    else:
        form = MovieForm()
        
    context = {
        'form' : form,
    }

    return render(request, 'movies/create.html', context)

def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '글이 성공적으로 수정되었습니다.',fail_silently=True,)
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
        
    context = {
        'form' : form,
        'movie' : movie,
    }

    return render(request, 'movies/update.html', context)

def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()

    return redirect('movies:index')