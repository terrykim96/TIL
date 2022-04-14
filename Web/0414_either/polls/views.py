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
    return render(request, 'polls/index.html', context)

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
            return redirect('polls:index')
    else:
        form = PostForm() # unbound form
    
    context = {
        'form': form,
    }
    return render(request, 'polls/new.html', context)

def detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk)
    
    # 조회수 증가
    post.views += 1
    post.save()
    
    context = {
        'post': post,
    }
    return render(request, 'polls/detail.html', context)