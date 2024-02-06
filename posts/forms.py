from django import forms
from . models import post 
from  posts.models import comment


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name','email','body']