# Generated by Django 3.1.1 on 2020-09-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterCloneApp', '0003_remove_twtweet_tw_sno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twtweet',
            name='frt_reg_date',
        ),
        migrations.AlterField(
            model_name='twtweet',
            name='tw_psno',
            field=models.IntegerField(null=True),
        ),
    ]