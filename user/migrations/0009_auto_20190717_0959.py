# Generated by Django 2.2.3 on 2019-07-17 09:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190716_0710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(max_length=140, verbose_name='О вас:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_like_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
