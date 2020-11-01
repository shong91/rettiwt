from django import forms
from django.forms import ModelForm
from twitterCloneApp.authmodel import TwUser
from twitterCloneApp.models import TwTweet, TwImages
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


class TwUserProfileForm(ModelForm):
    class Meta:
        model = TwUser
        fields = ['user_nm', 'user_birthday', 'user_acc_pub_yn']
        labels = {
            'user_nm': _('닉네임')
            # , 'user_prof_pic': _('이미지 url')
            # , 'user_prof_bio': _('바이오 이미지 url')
            , 'user_birthday': _('생년월일')
            , 'user_acc_pub_yn': _('계정 공개 여부')
        }


class TwTweetForm(ModelForm):
    class Meta:
        model = TwTweet
        fields = ['user', 'tw_content']
        labels = {
            'tw_content': _('내용')
        }
        widgets = {
            'user': forms.HiddenInput()
        }


class TwImageForm(ModelForm):
    image = forms.ImageField(label='이미지')

    class Meta:
        model = TwImages
        fields = ('image',)