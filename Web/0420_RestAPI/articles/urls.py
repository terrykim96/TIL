from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/api/v1/articles/
    path('', views.article_list),

    # http://localhost:8000/api/v1/articles/
    path('<int:pk>/', views.article_detail),

    path('<int:article_pk>/comments/', views.comment_list),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),
]