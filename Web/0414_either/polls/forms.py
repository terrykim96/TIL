from django import forms 
from .models import Vote, Comment


class VoteForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={
        "class" : 'form-control',
    }))

    choice_a = forms.CharField(widget= forms.TextInput(attrs={
        "class" : 'form-control',
    }))

    choice_b = forms.CharField(widget= forms.TextInput(attrs={
        "class" : 'form-control',
    }))

    class Meta:
        model = Vote
        # fields에 작성하는 목록은
        # 1) 사용자에게 html form에서 보여주고 싶은 것
        # 2) 유효성 검사를 진행하고 싶은 것을 작성
        fields = ('title', 'choice_a', 'choice_b')

class CommentForm(forms.ModelForm):
    pick = forms.ChoiceField(choices=(('------선택-------', '------선택-------'),('blue','blue'), ('red','red')), widget= forms.Select(
        attrs={
            'class' : 'form-control',
        }
    ))
    content = forms.CharField(widget= forms.TextInput(attrs={
        "class" : 'form-control',
    }))

    class Meta:
        model = Comment
        fields = ('pick', 'content')