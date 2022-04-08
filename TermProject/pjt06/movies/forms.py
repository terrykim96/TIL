from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    score = forms.FloatField(min_value=0.0, max_value=5.0, widget=forms.NumberInput(attrs={'class':'form-control', 'step':'0.5'}))
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title'
            }
        )
    )
    audience = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}))
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
        fields = ('title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description')