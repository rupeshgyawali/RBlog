# Generated by Django 2.0.7 on 2018-07-24 16:59

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_auto_20180724_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover_pic',
            field=models.ImageField(default='1.jpg', upload_to=post.models.cover_picture),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
