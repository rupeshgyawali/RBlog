# Generated by Django 2.0.7 on 2018-07-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_remove_userprofile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='_userprofile_followers_+', to='post.UserProfile'),
        ),
    ]
