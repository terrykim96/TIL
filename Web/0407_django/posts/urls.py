from django.urls import path 
from . import views 

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:pk>/<str:slug>/', views.detail, name='detail'), # 반드시 맨 아래
]