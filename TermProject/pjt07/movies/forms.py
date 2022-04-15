from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title'
            }
        )
    )
    poster_url = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the poster_url'
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the description'
            }
        )
    )

    class Meta:
        model = Movie
        fields = ('title', 'poster_url', 'description')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        exclude = ('user', 'movie')
