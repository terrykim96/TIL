# Project04. 프레임워크를 활용한 웹 페이지 구현

1. 목표

- HTML&CSS를 통한 웹 페이지 마크업 및 스타일링  
- Bootstrap 컴포넌트 및 그리드 시스템을 활용한 반응형 레이아웃 구성 
- Django web framework를 활용한 웹 서버 구성 
- Django Template System을 활용한 웹 페이지 마크업



Django와 html을 이용하여 영화 추천 페이지를 생성하는 프로젝트였다.

처음에 많이 헤맸지만 페어의 도움으로 시작할 수 있었다.

Django는 url - views - html 흐름으로 코드를 작성한다. 먼저 url.py에서 사용자의 요구사항을 받으면 views.py 내의 어떤 동작을 수행할지를 정해준다. 그 후 views.py에서 html로 정보를 넘겨 html에서 사용자에게 보여질 정보를 표현한다.

오늘 만든 페이지는 총 2개였다. 여러 영화의 기본 정보, 스틸컷 들을 보여주는 메인 페이지와 쇼생크 탈출 관련 추천 영화에 대해 소개하는 영화 추천 페이지. 

가장 먼저 두 페이지의 상위 페이지 설정을 위해 base.html을 이용했다.

base.html 페이지에서 navbar와 footer 부분을 만들고 {% block content %}을 이용하여 다른 html과 연결할 수 있도록 해주었다.

