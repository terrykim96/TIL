from django.urls import path, include
from . import views

# http://localhost:8000/articles/

app_name = 'articles'

urlpatterns = [
    # http://localhost:8000/articles/
    path('', views.index, name='index'),

    path('new/', views.new, name='new'),

]