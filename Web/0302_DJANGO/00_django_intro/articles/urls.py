from django.urls import path
from . import views


urlpatterns = [
    # http://127.0.0.1:8000
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('dtl-practice/', views.dtl_practice),

    # http://127.0.0.1:8000/throw/
    # 사용자가 입력할 수 있는 form을 보여주는 주소
    path('throw/', views.throw),

    # throw에서 보낸 정보를 받아서 화면에 보여주는 URL
    path('catch/', views.catch),

    # variable routing
    path('greeting/<str:name>/', views.dynamic_greeting),
]
