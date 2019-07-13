# Generated by Django 2.2.3 on 2019-07-12 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='comment',
            field=models.ManyToManyField(blank=True, related_name='_user_comment_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='_user_like_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
