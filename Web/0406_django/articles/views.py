from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

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

def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    """
    게시글 수정하는 함수
    - GET: 게시글 수정 form이 담긴 템플릿 반환
    - POST: 사용자가 수정한 게시글 DB 저장
    """
     # 현재 수정하고자 하는 게시글 DB에서 가져오기
    article = get_object_or_404(Article, pk=pk)

    # 만약 POST 요청이라면
    if request.method == 'POST':
        # 사용자가 보낸 정보 (request.POST)와
        # 기존 게시글 정보(instance=article)를 form에 바인딩
        form = ArticleForm(request.POST, instance=article)
        
        # 유효성 검사
        if form.is_valid():
            form.save() # 통과 후 DB 저장
            return redirect('articles:detail', article.pk)
    
    else:
        # 만약 GET 요청이라면
        # 기존 게시글 정보(instance=article)만 바인딩
        form = ArticleForm(instance=article)
    
    context = {
        'form': form,
    }
    return render(request, 'articles/edit.html', context)