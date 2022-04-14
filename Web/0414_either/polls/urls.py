from django.urls import path
from . import views 

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/<str:slug>/', views.detail, name='detail'),
]