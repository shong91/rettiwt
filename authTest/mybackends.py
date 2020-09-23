from django.contrib.auth.backends import BaseBackend
from authTest.models import User
from django.contrib.auth.hashers import (
    check_password, make_password
)


class MyBackend(BaseBackend):
    def authenticate(self, request, user_id=None, user_pwd=None): #**kwargs
        user = User.objects.get(user_id=user_id)
        if check_password(user_pwd, user.user_pwd):
            return user
        else:
            raise Exception

    def get_user(self, user_id):
        user = User.objects.get(user_id=user_id)
        if user:
            return user
        else:
            return None
