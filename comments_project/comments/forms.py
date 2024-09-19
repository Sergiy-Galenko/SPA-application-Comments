from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'email', 'homepage', 'captcha', 'text']

    captcha = forms.CharField(max_length=6, required=True)
