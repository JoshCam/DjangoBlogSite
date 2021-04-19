from django import forms

from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': '', 'text': ''} # to add lables to input box fill in blank strings
        