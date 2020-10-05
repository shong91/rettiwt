# Generated by Django 3.1.1 on 2020-10-04 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitterCloneApp', '0004_auto_20200927_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twact',
            old_name='qt_user_id',
            new_name='qt_user',
        ),
        migrations.RenameField(
            model_name='twact',
            old_name='rt_user_id',
            new_name='rt_user',
        ),
        migrations.RenameField(
            model_name='twact',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='twfollowuser',
            old_name='follower_user_id',
            new_name='follower_user',
        ),
        migrations.RenameField(
            model_name='twfollowuser',
            old_name='following_user_id',
            new_name='following_user',
        ),
        migrations.RenameField(
            model_name='twfollowuser',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='twtweet',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='twact',
            name='like_user_id',
        ),
        migrations.AddField(
            model_name='twact',
            name='like_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]