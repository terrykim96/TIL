from django import forms 
from .models import Post


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post 
        # fields에 작성하는 목록은
        # 1) 사용자에게 html form에서 보여주고 싶은 것
        # 2) 유효성 검사를 진행하고 싶은 것을 작성
        fields = ('title', 'content', 'image') 