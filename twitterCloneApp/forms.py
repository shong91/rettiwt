from django import forms
from django.forms import ModelForm
from twitterCloneApp.authmodel import TwUser
from twitterCloneApp.models import TwTweet
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


class TwTweetForm(ModelForm):
    class Meta:
        model = TwTweet
        fields = ['user_id', 'tw_content']
        labels = {
            'tw_content': _('내용')
            , 'tw_image_url': _('이미지 url')
            , 'tw_image_url': _('gif 이미지 url')
        }
        widgets = {
            'user_id': forms.HiddenInput()
        }