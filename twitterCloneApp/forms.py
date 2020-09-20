from django import forms
from django.forms import ModelForm
from twitterCloneApp.models import TwUser
from django.utils.translation import gettext_lazy as _


class TwJoinForm(ModelForm):
    class Meta:
        model = TwUser
        fields = ['user_id', 'user_nm', 'user_email', 'user_pwd']
        labels = {
            'user_id': _('아이디')
            , 'user_nm': _('이름')
            , 'user_email': _('이메일 주소')
            , 'user_pwd': _('비밀번호')
        }
        # help_text = {
        #     'user_id': _('아이디를 입력해주세요. ')
        #     , 'user_nm': _('이름을 입력해주세요. ')
        #     , 'user_email': _('이메일 주소를 입력해주세요. ')
        #     , 'user_pwd': _('비밀번호를 입력해주세요. ')
        # }
        widgets = {
            'user_pwd': forms.PasswordInput()
            , 'user_email': forms.EmailInput()
        }
        # error_messages = {
        #     'user_id': _('아이디는 최대 30자로 설정 가능합니다. ')
        #     , 'user_nm': _('이름은 최대 15자로 설정 가능합니다.  ')
        #     , 'user_email': _('이메일 형식이 잘못되었습니다. ')
        #     , 'user_pwd': _('비밀번호는 6자 이상 12자 이하, 영문+숫자 조합이어야 합니다.')
        # }


class TwLoginForm(ModelForm):
    class Meta:
        model = TwUser
        fields = ['user_id', 'user_pwd']
        labels = {
            'user_id': _('아이디')
            , 'user_pwd': _('비밀번호')
        }
        # help_text = {
        #     'user_id': _('아이디를 입력해주세요. ')
        #     , 'user_pwd': _('비밀번호를 입력해주세요. ')
        # }
        widgets = {
            'user_pwd': forms.PasswordInput()
        }
        # error_messages = {
        #     'user_id': _('아이디는 최대 30자로 설정 가능합니다. ')
        #     , 'user_pwd': _('비밀번호를 입력해주세요. ')
        # }