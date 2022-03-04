import random
from django.shortcuts import render

# Create your views here.

# index 함수는
# 어떠한 작업을 하고 (아직 쓰지 않음)
# index.html을 랜더링할 것이다.
def index(request):

    return render(request, 'index.html')

def recommendation(requests):
    context = {

    }
    return render(requests, 'recommendation.html', context)