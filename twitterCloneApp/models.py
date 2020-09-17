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
    FRT_REG_DATE = models.DateTimeField(max_length=8)
    LAST_USER_ID = models.CharField(max_length=30)
    LAST_CHG_DATE = models.DateTimeField(max_length=8)
