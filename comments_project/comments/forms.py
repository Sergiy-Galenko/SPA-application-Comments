from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    captcha = forms.CharField(max_length=6, required=True, help_text="Введіть CAPTCHA")
    parent = forms.ModelChoiceField(queryset=Comment.objects.all(), widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Comment
        fields = ['username', 'email', 'homepage', 'captcha', 'text', 'image', 'file', 'parent']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isalnum():
            raise forms.ValidationError("Ім'я користувача може містити лише цифри і літери.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError("Введіть коректний email.")
        return email

    def clean_homepage(self):
        homepage = self.cleaned_data.get('homepage')
        if homepage and not homepage.startswith('http'):
            raise forms.ValidationError("URL має починатися з http або https.")
        return homepage
