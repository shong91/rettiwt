from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.base_user import AbstractBaseUser

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

# my_auth.py
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserBackend(object):
    def authenticate(self, user_id, user_pwd):
        user = UserModel.objects.get(user_id=user_id)
        print(user)
        # 여기서는 user.password를 저장하는 의미가 없음.(장고가 관리 못함)
        return user

    def user_can_authenticate(self, user):
        is_active = getattr(user, 'is_active', None) # 유저가 활성화 되었는지
        return is_active or is_active is None # 유저가 없는 경우 is_active는 None이므로 True

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id) # 유저를 pk로 가져온다
        except UserModel.DoesNotExist:
            return None


class UserManager(BaseUserManager): #BaseUserManager
    def create_user(self, user_id, user_nm, user_email, user_pwd):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        print(user_id, '/ ', user_nm, '/ ',user_email, '/ ',user_pwd)
        if not user_id:
            raise ValueError(_('Users must have an user_id'))
        user = self.model(
            user_id=user_id,
            user_nm=user_nm,
            user_email=self.normalize_email(user_email),
            user_pwd=user_pwd
        )

        user.set_password(user_pwd)
        user.save(using=self._db)
        print('3', user.user_pwd)
        return user

    def create_superuser(self, user_id, user_nm, user_email, user_pwd):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다.
        """
        user = self.create_user(
            user_id=user_id,
            user_nm=user_nm,
            user_email=user_email,
            user_pwd=user_pwd
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create your models here.
# null=True 를 설정하지 않을 경우, 디폴트로 not null 임.
# Foreign key 설정 시 related_name 옵션에 대하여:
# (Reference) https://velog.io/@brighten_the_way/Django%EC%99%80-Reverse-relations%EA%B3%BC-Relatedname
class TwUser(AbstractBaseUser):
    user_id = models.CharField(max_length=30, help_text=help_text.get('user_id'), error_messages=error_messages)
    user_nm = models.CharField(max_length=45, help_text=help_text.get('user_nm'), error_messages=error_messages)
    user_email = models.CharField(max_length=100, help_text=help_text.get('user_email'), error_messages=error_messages)
    user_telno = models.CharField(max_length=12, default=None, null=True)
    user_birthday = models.CharField(max_length=8)
    user_pwd = models.CharField(max_length=128, help_text=help_text.get('user_pwd'), error_messages=error_messages)
    user_auth_yn = models.CharField(max_length=1, default="N")
    user_acc_pub_yn = models.CharField(max_length=1, default="Y")
    user_prof_pic = models.CharField(max_length=500)
    user_prof_bio = models.CharField(max_length=500)
    data_del_yn = models.CharField(max_length=1, default="N")
    frt_user_id = models.CharField(max_length=30)
    frt_reg_date = models.DateTimeField(auto_now_add=True)
    last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'user_id'
    PASSWORD_FIELD = 'user_pwd'


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
# python manage.py makemigrations
# python manage.py migrate
