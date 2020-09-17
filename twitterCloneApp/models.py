from django.db import models

# Create your models here.
class TwUser(models.Model):
    USER_NM = models.CharField(max_length=150)
    USER_EMAIL = models.CharField(max_length=100)
    USER_TELNO = models.CharField(max_length=12)
    USER_BIRTHDAY = models.CharField(max_length=8)
    USER_PWD = models.CharField(max_length=128)
    USER_AUTH_YN = models.CharField(max_length=1)
    USER_ACC_PUB_YN = models.CharField(max_length=1)
    USER_PROF_PIC = models.CharField(max_length=500)
    USER_PROF_BIO = models.CharField(max_length=500)
    DATA_DEL_YN = models.CharField(max_length=1)
    FRT_USER_ID = models.CharField(max_length=30)
    FRT_REG_DATE = models.DateTimeField(auto_now_add=True)
    LAST_USER_ID = models.CharField(max_length=30)
    LAST_CHG_DATE = models.DateTimeField(auto_now=True)



class TwFollowUser(models.Model):
    FOLLOW_SNO = models.IntegerField()
    USER_ID = models.CharField(max_length=30)
    FOLLOWING_USER_ID = models.CharField(max_length=30)
    FOLLOWER_USER_ID = models.CharField(max_length=30)
    DATA_DEL_YN = models.CharField(max_length=1)
    FRT_USER_ID = models.CharField(max_length=30)
    FRT_REG_DATE = models.DateTimeField(auto_now_add=True)
    LAST_USER_ID = models.CharField(max_length=30)
    LAST_CHG_DATE = models.DateTimeField(auto_now=True)


class TwTweet(models.Model):
    TW_SNO = models.IntegerField()
    TW_PSNO = models.CharField(max_length=10)
    USER_ID = models.CharField(max_length=30)
    TW_CONTENT = models.CharField(max_length=500)
    TW_IMAGE_URL = models.CharField(max_length=500)
    TW_GIF_URL = models.CharField(max_length=500)
    DATA_DEL_YN = models.CharField(max_length=1)
    FRT_USER_ID = models.CharField(max_length=30)
    FRT_REG_DATE = models.DateTimeField(auto_now_add=True)
    LAST_USER_ID = models.CharField(max_length=30)
    LAST_CHG_DATE = models.DateTimeField(auto_now=True)



