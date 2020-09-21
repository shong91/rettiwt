from django import forms
# from django.contrib.auth.models import User
from authTest.models import User
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


# using Custom User class (authTest.models)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'user_nm', 'user_email', 'user_pwd']
        labels = {
             'user_id': _('아이디')
             , 'user_nm': _('이름')
             , 'user_email': _('이메일 주소')
             , 'user_pwd': _('비밀번호')
        }
        widgets = {
            'password': forms.PasswordInput()
            , 'user_email': forms.EmailInput()
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'user_pwd']
        labels = {
            'user_id': _('아이디')
            , 'user_pwd': _('비밀번호')
        }
        widgets = {
            'password': forms.PasswordInput()
        }


# using Default User class (django.contrib.auth.models)
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'password']
#         labels = {
#             'username': _('아이디')
#             , 'email': _('이메일 주소')
#             , 'password': _('비밀번호')
#         }
#         widgets = {
#             'password': forms.PasswordInput()
#         }
#
#
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         labels = {
#             'username': _('아이디')
#             , 'password': _('비밀번호')
#         }
#         widgets = {
#             'password': forms.PasswordInput()
#         }