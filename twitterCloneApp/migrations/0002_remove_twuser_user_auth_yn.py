# Generated by Django 3.1.1 on 2020-09-26 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterCloneApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twuser',
            name='user_auth_yn',
        ),
    ]