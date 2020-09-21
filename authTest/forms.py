from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        labels = {
            'username': _('아이디')
            , 'email': _('이메일 주소')
            , 'password': _('비밀번호')
        }
        widgets = {
            'password': forms.PasswordInput()
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': _('아이디')
            , 'password': _('비밀번호')
        }
        widgets = {
            'password': forms.PasswordInput()
        }