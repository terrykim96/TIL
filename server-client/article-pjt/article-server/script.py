"""
Django 환경 설정 필수)
https://docs.djangoproject.com/en/4.0/topics/settings/#using-settings-without-setting-django-settings-module

실행 방법)
python script.py

python manage.py runserver
"""
from articles.models import Article 

# 1. 수집한 데이터 불러오기
# API, CSV 파일...
# articles = [...]

# 2. Article 테이블에 넣기
# Tip. 한 번에 여러개 넣을 때는 bulk_create 사용
# for article in articles:
#     Article.objects.create(
#         title=article.title,
#         ...
#     )