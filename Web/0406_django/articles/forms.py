from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # 유효성 검사를 진행할 필드
        fields = ('title', 'content')