import urllib
import requests

#이미지 저장
Base_URL = 'https://korea-webtoon-api.herokuapp.com'
path = '/all'
response = requests.get(Base_URL+path)
webtoons_popular = response.json()
i = 0
for webtoon in webtoons_popular:
    urllib.request.urlretrieve(webtoon['img'], f"{webtoon['title']}.jpg")
    i += 1