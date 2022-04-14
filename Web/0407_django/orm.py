"""
ORM 기초 RECAP
"""
# 1. 전체 게시글 불러오기
# QuerySet 반환
posts = Post.objects.all()

# 2. 특정 게시글 불러오기 
# 단일 객체 반환
post = Post.objects.get(pk=1)

# 해당하는 데이터가 하나여도 쿼리셋 반환
post = Post.objects.filter(pk=1)

# 3. 데이터 생성
# 첫번째 
Post.objects.create(title='', content='')

# 두번째
post = Post()
post.title = ''
post.content = ''
post.save()

"""
ORM (1:N)
"""
# N => 1 참조하기
# 자식에서 부모 참조하기

## 예시)
## 1번 댓글의 부모 게시글 확인하기
comment = Comment.objects.get(pk=1)
comment.post 

## 1번 댓글의 부모 게시글의 제목 확인하기
comment.post.title 

# 1 => N 참조하기
# 부모에서 자식 테이블 참조하기

# 양식)
# 부모테이블명.자식테이블명_set.QuerySetAPI

## 예시)
## 1번 게시글에 달린 모든 댓글 가져오기
post = Post.objects.get(pk=1)
comments = post.comment_set.all()

## 1번 게시글에 달린 댓글 중...
## 2번 댓글의 내용 출력하기
comment_two = post.comment_set.get(pk=2)
print(comment_two.content) 

"""
ORM (1:N) 
Forward Access
Backward Access 
"""

# Forward Access (자식 => 부모)
# 자식.FK필드_이름
comments = Comment.objects.all()
comment = comments[0]
comment.post # Forward Access 

# Backward Access (부모 => 자식, 역참조)
# 부모객체.자식테이블명_set.QuerySetAPI
posts = Post.objects.all()
post = posts[0]

comments = post.comment_set.all()

# Backward Access 커스터마이징
# related_name 설정을 통해 가능
# 만약, related_name이 comments라면...
posts = Post.objects.all()
post = posts[0]

comments = post.comments.all()

