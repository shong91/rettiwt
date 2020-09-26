from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password
)


class UserManager(BaseUserManager):
    user_in_migrations = True

    # 일반 user 생성 함수
    def create_user(self, user_id, user_nm, user_email, user_pwd=None):
        if not user_id:
            raise ValueError('Must have user id')

        user_email = self.normalize_email(user_email)

        user = self.model(
            user_id=user_id,
            user_nm=user_nm,
            user_email=user_email,
            user_pwd=make_password(user_pwd)
        )

        # user.set_password(user_pwd)
        user.save(using=self._db)

        return user

    # 관리자 user 생성 함수
    def create_superuser(self, user_id, user_nm, user_email, user_pwd):
        user = self.create_user(
            user_id=user_id,
            user_nm=user_nm,
            user_email=self.normalize_email(user_email),
            user_pwd=user_pwd
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class TwUser(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    user_id = models.CharField(max_length=30) #, help_text=help_text.get('user_id'), error_messages=error_messages)
    user_nm = models.CharField(max_length=45) #, help_text=help_text.get('user_nm'), error_messages=error_messages)
    user_email = models.CharField(max_length=100) #, help_text=help_text.get('user_email'), error_messages=error_messages)
    user_pwd = models.CharField(max_length=128) #, help_text=help_text.get('user_pwd'), error_messages=error_messages)

    user_telno = models.CharField(max_length=12, default=None, null=True)
    user_birthday = models.CharField(max_length=8)
    user_acc_pub_yn = models.CharField(max_length=1, default="Y")
    user_prof_pic = models.CharField(max_length=500)
    user_prof_bio = models.CharField(max_length=500)

    # is_active , is_admin 은 Django 유저 모델의 필수 필드이기 때문에 반드시 정의되어야 한다.
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # 공통컬럼
    data_del_yn = models.CharField(max_length=1, default="N")
    frt_user_id = models.CharField(max_length=30)
    # date_joined으로 대체: frt_reg_date = models.DateTimeField(auto_now_add=True)
    last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)

    # 커스텀 User model 의 unique identifier
    USERNAME_FIELD = 'user_id'
    PASSWORD_FIELD = 'user_pwd'
    REQUIRED_FIELDS = ['user_nm', 'user_email']  # python manage.py superuser 로 관리자계정 생성 시 필요한 필드들 명시시
