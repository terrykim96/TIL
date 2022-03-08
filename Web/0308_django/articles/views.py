from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 1. DB에서 게시글 목록을 전부 가져온다.
    
    # 파이썬 방식의 정렬
    # article_list = Article.objects.all()[::-1]

    # DB 레벨에서의 정렬
    article_list = Article.objects.order_by('-created_at')

    # 2. 게시글 목록을 context에 담아서 넘긴다.
    context = {
        'article_list': article_list,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html') 


def create(request):
    # 1. 사용자가 보낸 게시글 정보를 꺼낸다.
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 2. DB에 저장한다.
    article = Article()
    article.title = title 
    article.content = content 
    article.save()
    
    # 3. 글 목록(또는 디테일 페이지)을 응답한다.
    return redirect('articles:index') 


def detail(request, article_pk):
    # article_pk: 사용자가 요청한 게시글의 pk
    article = Article.objects.get(pk=article_pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context) 


def delete(request, article_pk):
    # 1. 삭제하려는 게시글을 가져온다.
    article = Article.objects.get(pk=article_pk)
    
    # 2. 삭제한다.
    # (이 시점에서 DB 반영)
    article.delete()

    # 3. 메인으로 보낸다. (리다이렉트)
    return redirect('articles:index') 