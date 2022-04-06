from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    # ORM 양식: ClassName.objects.QuerysetAPI
    articles = Article.objects.all() # QuerySet (유사 리스트)
    context ={
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def new(request):
    '''
    게시글 작성하는 함수
    - GET: 게시글 작성 form이 담긴 템플릿 반환
    - POST: 사용자가 작성한 게시글 DB 저장
    '''

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Article.objects.create(title=title, content=content) # DB 저장

        return redirect('articles:index')

    else:
        return render(request, 'articles/new.html')