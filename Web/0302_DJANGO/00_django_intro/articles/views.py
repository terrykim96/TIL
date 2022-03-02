import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Alice',
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'greeting.html', context)


def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    context = {
        'foods': foods,
        'pick': pick,
    }
    return render(request, 'dinner.html', context)


def dtl_practice(request):
    foods = ['짜장면', '탕수육', '짬뽕', '양장피']
    fruits = ['apple', 'banana', 'cucumber', 'mango']
    user_list = []
    context = {
        'foods': foods,
        'fruits': fruits,
        'user_list': user_list,
    }
    return render(request, 'dtl_practice.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # 1. 사용자가 보낸 데이터를 꺼낸다.
    message = request.GET.get('message')

    # 2. 그 데이터를 html (템플릿)에 넘긴다.
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)

def dynamic_greeting(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'dynamic_greeting.html', context)