# Generated by Django 2.0.7 on 2018-07-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20180724_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='post.UserProfile'),
        ),
    ]
