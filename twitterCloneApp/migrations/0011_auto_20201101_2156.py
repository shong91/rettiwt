# Generated by Django 3.1.1 on 2020-11-01 12:56

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('twitterCloneApp', '0010_auto_20201012_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twimages',
            old_name='twTweet',
            new_name='tweet',
        ),
        migrations.RemoveField(
            model_name='twact',
            name='frt_reg_date',
        ),
        migrations.RemoveField(
            model_name='twact',
            name='frt_user_id',
        ),
        migrations.RemoveField(
            model_name='twact',
            name='last_user_id',
        ),
        migrations.RemoveField(
            model_name='twfollowuser',
            name='frt_reg_date',
        ),
        migrations.RemoveField(
            model_name='twfollowuser',
            name='frt_user_id',
        ),
        migrations.RemoveField(
            model_name='twfollowuser',
            name='last_user_id',
        ),
        migrations.RemoveField(
            model_name='twtweet',
            name='frt_user_id',
        ),
        migrations.RemoveField(
            model_name='twtweet',
            name='last_user_id',
        ),
        migrations.RemoveField(
            model_name='twuser',
            name='frt_user_id',
        ),
        migrations.RemoveField(
            model_name='twuser',
            name='last_user_id',
        ),
        migrations.AlterField(
            model_name='twuser',
            name='user_prof_pic',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='user/'),
        ),
    ]
