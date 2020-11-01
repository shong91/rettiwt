from django.db import models
from django.utils.translation import gettext_lazy as _
from twitterCloneApp.authmodel import TwUser
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit

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
    user = models.ForeignKey(TwUser, on_delete=models.CASCADE, related_name="TwFollowUser_user_id", error_messages=None)            # PK = FK (identifying-relation)
    following_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, default=None, null=True, related_name="following_user_id")  # PK != FK (Non-identifying-relation)
    follower_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, default=None, null=True, related_name="follower_user_id")   # PK != FK (Non-identifying-relation)
    data_del_yn = models.CharField(max_length=1, default="N")
    # frt_user_id = models.CharField(max_length=30)
    # frt_reg_date = models.DateTimeField(auto_now_add=True)
    # last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)


class TwTweet(models.Model):
    # tw_sno = models.IntegerField() # id가 있는데 이게 필요할까?
    tw_psno = models.IntegerField(null=True)

    # FK 가 user_id 가 아니라 user_id_id 로 잡혀서 renaming 함
    user = models.ForeignKey(TwUser, on_delete=models.CASCADE, related_name="TwTweet_user_id", error_messages=None)
    tw_content = models.CharField(max_length=500)

    # save as Origin
    # tw_image_url = models.ImageField(upload_to='img/', null=True, blank=True)

    # - ProcessedImageField: django-orm이 인식하는 처리된 이미지 속성. image필드와 마찬가지로, 이미지가 저장된 위치를 DB에 저장
    # - ImageSpecField: 이미 생성된 이미지의 캐시용 이미지를 생성

    # 공통컬럼
    data_del_yn = models.CharField(max_length=1, default="N")
    # frt_user_id = models.CharField(max_length=30)
    # date_joined으로 대체: frt_reg_date = models.DateTimeField(auto_now_add=True)
    # last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['user', 'tw_content']


# 이미지 업로드 : 참조) https://the-boxer.tistory.com/41
# 멀티파일 업로드 : 참조) https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
class TwImages(models.Model):
    tweet = models.ForeignKey(TwTweet, blank=False, null=False, on_delete=models.CASCADE)
    # save resized version
    image =  ProcessedImageField(
        upload_to='img/',
        processors=[ResizeToFit(width=960, upscale=False)],
        format='JPEG',
        blank=True, null=True
    )


class TwAct(models.Model):
    tw_act_sno = models.IntegerField()
    user = models.ForeignKey(TwTweet, on_delete=models.CASCADE, related_name="TwAct_user_id", error_messages=None)
    rt_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="rt_user_id")
    qt_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="qt_user_id")
    like_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="like_user_id")
    data_del_yn = models.CharField(max_length=1, default="N")
    # frt_user_id = models.CharField(max_length=30)
    # frt_reg_date = models.DateTimeField(auto_now_add=True)
    # last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)


# 모델 생성/수정 후 마이그레이션
# python manage.py makemigrations (appname)
# python manage.py migrate
# python manage.py dbshell
