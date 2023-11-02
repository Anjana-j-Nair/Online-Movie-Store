# updating movie details
from django import forms
from .models import movies
class form_movie(forms.ModelForm):
    class Meta:
        model=movies
        fields=['name','desc','year','img']