# Generated by Django 3.1.1 on 2020-10-11 14:14

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('twitterCloneApp', '0006_auto_20201007_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twtweet',
            name='tw_image_url',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
