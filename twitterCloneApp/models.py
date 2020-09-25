from django.db import models
from django.utils.translation import gettext_lazy as _
from twitterCloneApp.authmodel import TwUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password
)
error_messages = {
    'user_id': _('아이디는 최대 30자로 설정 가능합니다. ')
    , 'user_nm': _('이름은 최대 15자로 설정 가능합니다.  ')
    , 'user_email': _('이메일 형식이 잘못되었습니다. ')
    , 'user_pwd': _('비밀번호는 6자 이상 12자 이하, 영문+숫자 조합이어야 합니다.')
    }

help_text = {
    'user_id': _('아이디를 입력해주세요. ')
    , 'user_nm': _('이름을 입력해주세요. ')
    , 'user_email': _('이메일 주소를 입력해주세요. ')
    , 'user_pwd': _('비밀번호를 입력해주세요. ')
}


class TwFollowUser(models.Model):
    # follow_sno = models.IntegerField() # id가 있는데 이게 필요할까?
    # Many to One Relation: Foreign key 설정
    user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, related_name="TwFollowUser_user_id", error_messages=None)            # PK = FK (identifying-relation)
    following_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, default=None, null=True, related_name="following_user_id")  # PK != FK (Non-identifying-relation)
    follower_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, default=None, null=True, related_name="follower_user_id")   # PK != FK (Non-identifying-relation)
    data_del_yn = models.CharField(max_length=1, default="N")
    frt_user_id = models.CharField(max_length=30)
    frt_reg_date = models.DateTimeField(auto_now_add=True)
    last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)


class TwTweet(models.Model):
    tw_sno = models.IntegerField()
    tw_psno = models.IntegerField()
    user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, related_name="TwTweet_user_id", error_messages=None)
    tw_content = models.CharField(max_length=500)
    tw_image_url = models.CharField(max_length=500, default=None, null=True)
    tw_gif_url = models.CharField(max_length=500, default=None, null=True)
    data_del_yn = models.CharField(max_length=1, default="N")
    frt_user_id = models.CharField(max_length=30)
    frt_reg_date = models.DateTimeField(auto_now_add=True)
    last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)


class TwAct(models.Model):
    tw_act_sno = models.IntegerField()
    user_id = models.ForeignKey(TwTweet, on_delete=models.CASCADE, related_name="TwAct_user_id", error_messages=None)
    rt_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="rt_user_id")
    qt_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="qt_user_id")
    like_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE)
    data_del_yn = models.CharField(max_length=1, default="N")
    frt_user_id = models.CharField(max_length=30)
    frt_reg_date = models.DateTimeField(auto_now_add=True)
    last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)


# 모델 생성/수정 후 마이그레이션
# python manage.py makemigrations (appname)
# python manage.py migrate
