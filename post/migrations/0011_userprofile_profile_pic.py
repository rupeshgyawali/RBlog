# Generated by Django 2.0.7 on 2018-07-23 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]
