from django.http import HttpResponse
from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from .models import Post 
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required 
@require_http_methods(['GET', 'POST'])
def new(request):
    """
    글쓰기 (ModelForm)
    - GET: 폼이 담긴 템플릿 반환
    - POST: 사용자 요청 정보 유효성 검사 & 저장
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # bound form
        if form.is_valid():                          # 유효성 검사
            form.save()                              # DB 저장
            messages.add_message(request, messages.INFO, '글이 성공적으로 작성되었습니다.')
            return redirect('posts:index')
    else:
        form = PostForm() # unbound form
    
    context = {
        'form': form,
    }
    return render(request, 'posts/new.html', context)


def detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    
    # 조회수 증가
    post.views += 1
    post.save()
    
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


@login_required 
@require_http_methods(['GET', 'POST'])
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) 
        if form.is_valid():               
            form.save()                              
            return redirect('posts:detail', post.pk, post.slug)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
    }
    return render(request, 'posts/edit.html', context)


# @login_required # 로그인이 안되어있으면 => 로그인 페이지로 이동
@require_http_methods(['POST']) # POST 아니면 => 405 (Method Not Allowed) 에러 발생
def delete(request, pk):
    if not request.user.is_authenticated:
        # 401 == Unauthorized
        return HttpResponse('너 권한 없음...!', status=401) 
    
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.add_message(request, messages.ERROR, '글이 성공적으로 삭제되었습니다.')
    return redirect('posts:index')

