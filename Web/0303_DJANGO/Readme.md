# Django workshop 01

## 개발 환경 설정

- [x] 가상 환경 생성 (venv)

  - 가상 환경 활성화

    ```
    (windows)
    source venv/Scripts/activate
    
    (macOS)
    source venv/bin/activate
    ```

  

- [x] 프로젝트에 필요한 패키지 설치

  - Django **3.2.12**

    ```
    pip install django==3.2.12
    ```

- [x] 프로젝트 생성

  - Intro

    ```
    django-admin startproject intro .
    ```

- [x] 앱 생성

  > 앱 생성 시, settings.py의 INSTALLED_APPS에 반드시 출생 신고

  

## 기능 개발

### 유저 스토리

1. 사용자가 `/dinner/저녁메뉴/인원수/` 주소로 접속한다.

2. 사용자가 저녁 메뉴와 저녁 먹을 사람 정보가 담긴 페이지를 본다.

   

### 기능 정의

1. 사용자가 `/dinner/저녁메뉴/인원수/` 주소로 접속한다. 

   - [x] 사용자가 접속할 수 있는 주소를 작성한다. (urls.py)

- [x] 위 주소로 접속했을 때 실행할 함수를 작성한다. (views.py)
  - [x] 위 함수에서 저녁메뉴와 인원수 정보를 URL에서 가져온다. (views.py)
- [x] 위 함수에서 저녁메뉴와 인원수 정보를 template(html)에 넘긴다. (views.py)

2. 사용자가 저녁메뉴와 저녁 먹을 사람 정보가 담긴 페이지를 본다.
   - [x] view 함수에서 전달한 저녁메뉴와 인원수 정보를 template에서 보여준다. (template or dinner.html)







