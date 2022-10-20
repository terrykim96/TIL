import requests
from urllib import response
import urllib
import os

URL = 'https://korea-webtoon-api.herokuapp.com/naver'

response = requests.get(URL)
webtoons_popular = response.json()
print(webtoons_popular[0]['img'])
urllib.request.urlretrieve(webtoons_popular[0]['img'], "test.png")