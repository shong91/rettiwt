from django.db import models
from django.utils.translation import gettext_lazy as _
from twitterCloneApp.authmodel import TwUser
from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit


class TwFollowUser(models.Model):
    # follow_sno = models.IntegerField() # id가 있는데 이게 필요할까?
    # Many to One Relation: Foreign key 설정
    user = models.ForeignKey(TwUser, on_delete=models.CASCADE, related_name="TwFollowUser_user_id", error_messages=None)            # PK = FK (identifying-relation)
    following_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, default=None, null=True, related_name="following_user_id")  # PK != FK (Non-identifying-relation)
    follower_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, default=None, null=True, related_name="follower_user_id")   # PK != FK (Non-identifying-relation)
    data_del_yn = models.CharField(max_length=1, default="N")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TwTweet(models.Model):
    tw_psno = models.IntegerField(null=True)
    # FK 가 user_id 가 아니라 user_id_id 로 잡혀서 renaming 함
    user = models.ForeignKey(TwUser, on_delete=models.CASCADE, related_name="TwUser_user_id", error_messages=None)
    tw_content = models.CharField(max_length=500, null=False)
    image = ProcessedImageField(
        upload_to='img/',
        processors=[ResizeToFit(width=960, upscale=False)],
        format='JPEG',
        blank=True, null=True
    )
    # 공통컬럼
    data_del_yn = models.CharField(max_length=1, default="N")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['user', 'tw_content']
#     https://velog.io/@magnoliarfsit/ReDjango-8.-QuerySis%20named%20as%20the%20'USERNAME_FIELD',%20but%20it%20is%20not%20unique.et-Method-4


# 이미지 업로드 : 참조) https://the-boxer.tistory.com/41
# 멀티파일 업로드 : 참조) https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
class TwImages(models.Model):
    tweet = models.ForeignKey(TwTweet, blank=False, null=False, related_name="tweet_sno", on_delete=models.CASCADE)
    # save resized version
    image = ProcessedImageField(
        upload_to='img/',
        processors=[ResizeToFit(width=960, upscale=False)],
        format='JPEG',
        blank=True, null=True
    )
    # - ProcessedImageField: django-orm이 인식하는 처리된 이미지 속성. image필드와 마찬가지로, 이미지가 저장된 위치를 DB에 저장
    # - ImageSpecField: 이미 생성된 이미지의 캐시용 이미지를 생성


class TwAct(models.Model):
    tw_act_sno = models.IntegerField()
    user = models.ForeignKey(TwTweet, on_delete=models.CASCADE, related_name="TwAct_user_id", error_messages=None)
    rt_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="rt_user_id")
    qt_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="qt_user_id")
    like_user = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="like_user_id")
    data_del_yn = models.CharField(max_length=1, default="N")



# 모델 생성/수정 후 마이그레이션
# python manage.py makemigrations (appname)
# python manage.py migrate
# python manage.py dbshell
