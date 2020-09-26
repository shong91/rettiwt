from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ObjectDoesNotExist
from twitterCloneApp.authmodel import TwUser
from django.contrib.auth.hashers import (
    check_password, make_password
)


class MyBackend(BaseBackend):
    def authenticate(self, request, user_id=None, user_pwd=None): #**kwargs
        try:
            user = TwUser.objects.get(user_id=user_id)
            if check_password(user_pwd, user.user_pwd):     # 로그인 인증 성공
                return user
            else:                                           # 비밀번호 오류
                return None
        except ObjectDoesNotExist:                          # 해당 아이디 없음
            return None

    def get_user(self, user_id):
        user = TwUser.objects.get(user_id=user_id)
        if user:
            return user
        else:
            return None
