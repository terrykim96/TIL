from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts' : posts,
    }

    return render(request, 'posts/index.html', context)

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '글이 성공적으로 작성되었습니다.',fail_silently=True,)
            return redirect('posts:index')
    else:
        form = PostForm()
        
    context = {
        'form' : form,
    }

    return render(request, 'posts/new.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)

    # 조회수 증가
    post.views += 1
    post.save()

    context ={
        'post' : post,
    }
    return render(request, 'posts/detail.html', context)

def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '글이 성공적으로 작성되었습니다.',fail_silently=True,)
            return redirect('posts:index')
    else:
        form = PostForm(instance=post)
        
    context = {
        'form' : form,
    }

    return render(request, 'posts/edit.html', context)

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts:index')