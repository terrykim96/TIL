from django.shortcuts import render
import requests
import random

# Create your views here.

def dinner(request, menu, number):
    context = {
      'menu' : menu,
      'number' : number,
    }

    return render(request, 'dinner.html', context)

def lotto(request):
    my_nums = random.sample(range(1, 46), 6)

    context = {
        'my_nums' : my_nums
    }

    return render(request, 'lotto.html', context)