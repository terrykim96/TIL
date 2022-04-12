from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField()
    views = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        # title 정보를 slugify해서 저장
        self.slug = slugify(self.title, allow_unicode=True)
        
        # 부모 클래스에 정의된 save 호출
        super().save(*args, **kwargs)