from django.shortcuts import render
import requests
from urllib import response
import random

URL = 'https://api.themoviedb.org/3/movie/278/recommendations?api_key=96b45c1f564c7459d2fdf0183eb0070a&language=ko-KR&page=1'
    
response = requests.get(URL).json()
data = response.get('results')
rand_num = random.randint(0, len(response) - 1)

context ={
    'title' : data[rand_num].get('title'),
    'overview' : data[rand_num].get('overview'),
    'poster_path' : 'https://www.themoviedb.org/t/p/w1280' + data[rand_num].get('poster_path'),
    'vote_average' : data[rand_num].get('vote_average'),
}

print(context)