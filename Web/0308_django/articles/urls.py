from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
    # 게시글 리스트를 보여주는 URL
    # http://127.0.0.1:800/articles/
    path('', views.index, name='index'),    

    # 게시글 폼이 담긴 페이지를 보여주는 URL
    path('new/', views.new, name='new'),
    
    # 작성한 게시글을 저장하는 URL
    path('create/', views.create, name='create'),
    
    # 게시글 상세 페이지
    # ex) http://127.0.0.1:8000/articles/1/
    path('<int:article_pk>/', views.detail, name='detail'),

    # 게시글 삭제
    path('<int:article_pk>/delete/', views.delete, name='delete'),

    # 게시글 수정 페이지 요청
    # ex) http://127.0.0.1.8000/articles/:pk/edit/
    path('<int:article_pk>/edit/', views.edit, name='edit'),

    # 게시글 수정 완료
    path('<int:article_pk>/update/', views.update, name='update')
]