# DB API (ORM)

[toc]



## DB API 구문 기초

- `ClassName`.`objects`.`QuerysetAPI`

  - 예시)

    ```
    Article.objects.all()
    ```



## QuerySet

> 유사 리스트처럼 조작합니다.

- 데이터베이스로부터 전달받은 객체의 "목록"



## CRUD

### CREATE

#### 첫번째 방법

```python
# 1. 클래스(모델 혹은 스키마)의 인스턴스를 만든다.
article = Article()

# 2. 인스턴스의 필드에 값을 채운다.
article.title = '제목제목'
article.content = '내용내용'

# 3. (중요) save 메서드를 통해 DB에 저장한다.
article.save()
```



#### 두번째 방법

```python
# 1. 클래스의 인스턴스를 만들 때 필드값을 같이 넘긴다.
article = Article(title='제목', content='내용')

# 2. (중요) save 메서드를 통해 DB에 저장한다.
article.save()
```



#### 세번째 방법

> create 메서드는 내부적으로 `save` 메서드를 호출합니다.
>
> 새로 생성된 객체를 "반환"합니다.

```python
# 1. create 메서드를 사용하여 save 없이 바로 DB에 저장한다.

article = Article.objects.create(title='제목', content='내용')
```



### READ

#### all()

- 해당 테이블의 모든 데이터를 가져와서 **QuerySet으로 반환합니다.**

```python
Article.objects.all()
```



#### get()

- 조건에 맞는 특정한 "단일" 데이터 객체를 반환합니다.

```python
article = Article.objects.get(id=1)

# 여러 개의 조건을 줄 수도 있습니다.
# 이 때의 조건은 AND 조건입니다.
article = Article.objects.get(id=3, title='제목')

# 데이터가 없을 경우 "에러"를 발생시킵니다.
article = Article.objects.get(id=1000)
```



#### filter()

- 지정된 조건에 일치하는 객체들을 가져와서 QuerySet으로 반환합니다.

```python
article_list = Article.objects.filter(id=3, title='제목')
#=> article_list는 현재 QuerySet (유사 리스트)

article = article_list[0]
title = article.title 
```



### UPDATE

```python
# 1. 수정하고자 하는 데이터를 가져온다.
article = Article.objects.get(id=1)

# 2. 수정한다.
article.title = '수정된 제목'

# 3. DB에 반영.
article.save()
```



### DELETE

```python
# 1. 삭제하고자 하는 데이터를 가져온다.
article = Article.objects.get(id=1)

# 2. 삭제. 끝.
article.delete() 
```



## Field Lookups

- SQL WHERE 절(clause)을 지정하는 방법

```python
Article.objects.filter(pk__gt=2)

Article.objects.filter(content__contains='제목')
```















