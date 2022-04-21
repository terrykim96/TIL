from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.artist_list),
    path('artists/<int:pk>/', views.artist_detail),
    path('artists/<int:pk>/music/', views.artist_music),
    path('music/', views.music_list),
    path('music/<int:pk>', views.music_detail),
]