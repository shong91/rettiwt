from django.db import models


# Create your models here.
# null=True 를 설정하지 않을 경우, 디폴트로 not null 임.
# Foreign key 설정 시 related_name 옵션에 대하여:
# (Reference) https://velog.io/@brighten_the_way/Django%EC%99%80-Reverse-relations%EA%B3%BC-Relatedname
class TwUser(models.Model):
    user_id = models.CharField(max_length=30)
    user_nm = models.CharField(max_length=45)
    user_email = models.CharField(max_length=100)
    user_telno = models.CharField(max_length=12, default=None, null=True)
    user_birthday = models.CharField(max_length=8)
    user_pwd = models.CharField(max_length=128)
    user_auth_yn = models.CharField(max_length=1, default="N")
    user_acc_pub_yn = models.CharField(max_length=1, default="Y")
    user_prof_pic = models.CharField(max_length=500)
    user_prof_bio = models.CharField(max_length=500)
    data_del_yn = models.CharField(max_length=1, default="N")
    frt_user_id = models.CharField(max_length=30)
    frt_reg_date = models.DateTimeField(auto_now_add=True)
    last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)


class TwFollowUser(models.Model):
    # follow_sno = models.IntegerField() # id가 있는데 이게 필요할까?
    # Many to One Relation: Foreign key 설정
    user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, related_name="TwFollowUser_user_id")            # PK = FK (identifying-relation)
    following_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="following_user_id")  # PK != FK (Non-identifying-relation)
    follower_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="follower_user_id")   # PK != FK (Non-identifying-relation)
    data_del_yn = models.CharField(max_length=1, default="N")
    frt_user_id = models.CharField(max_length=30)
    frt_reg_date = models.DateTimeField(auto_now_add=True)
    last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)


class TwTweet(models.Model):
    tw_sno = models.IntegerField()
    tw_psno = models.IntegerField()
    user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, related_name="TwTweet_user_id")
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
    user_id = models.ForeignKey(TwTweet, on_delete=models.CASCADE, related_name="TwAct_user_id")
    rt_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="rt_user_id")
    qt_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE, null=True, related_name="qt_user_id")
    like_user_id = models.ForeignKey(TwUser, on_delete=models.CASCADE)
    data_del_yn = models.CharField(max_length=1, default="N")
    frt_user_id = models.CharField(max_length=30)
    frt_reg_date = models.DateTimeField(auto_now_add=True)
    last_user_id = models.CharField(max_length=30)
    last_chg_date = models.DateTimeField(auto_now=True)
