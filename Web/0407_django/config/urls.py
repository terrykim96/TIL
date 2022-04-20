"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

def fake(request):
    import random 
    from faker import Faker
    from django.contrib.auth import get_user_model
    from posts.models import Post, Comment

    User = get_user_model()

    fake = Faker()

    for i in range(5):
        User.objects.create_user(
            fake.user_name(),
            fake.email(),
            '1q2w3e4r4r!',
        )

    for i in range(1, 11):
        Post.objects.create(
            title=f'테스트 {i}글',
            content=fake.text(),
            author_id=random.choice(range(1, 6))
        )
    
        for j in range(1, 10):
            Comment.objects.create(
                content=fake.sentence(),
                post_id=i,
                author_id=random.choice(range(1, 6))
            
            )
    
    from django.http import HttpResponse
    return HttpResponse('done')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # http://localhost:8000/
    path('', include('posts.urls')),

    path('accounts/', include('accounts.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('sample/', fake),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
