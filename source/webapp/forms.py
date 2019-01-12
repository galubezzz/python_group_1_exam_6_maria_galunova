from django import forms
from webapp.models import User, UserInfo, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =['author']

