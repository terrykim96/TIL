from django.db import models
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
class Hashtag(models.Model):
    content = models.CharField(max_length=10)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField()
    views = models.IntegerField(default=0)

    hashtags = models.ManyToManyField(Hashtag, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )
    
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank= True,
        related_name='like_posts',
    )

    def save(self, *args, **kwargs):
        # title 정보를 slugify해서 저장
        self.slug = slugify(self.title, allow_unicode=True)
        
        # 부모 클래스에 정의된 save 호출
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    하나의 게시글(1)에는 여러 개의 댓글(N)이 속할 수 있다.
    """
    # FK 필드의 이름은 "부모 테이블의 이름"으로 작성
    # FK 첫번째 인자: 부모 테이블
    # FK 두번째 인자: on_delete 옵션 설정 (참조 무결성)
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )

