from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/dinner/저녁메뉴/인원수/
    path('dinner/<str:menu>/<int:number>/', views.dinner, name="dinner"),

    path('lotto/', views.lotto, name='lotto'),
]