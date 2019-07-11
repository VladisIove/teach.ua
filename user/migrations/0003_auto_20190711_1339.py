# Generated by Django 2.2.3 on 2019-07-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190711_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='user',
            name='price_per_hource',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Цена в час'),
        ),
        migrations.AlterField(
            model_name='user',
            name='valid_announcement',
            field=models.BooleanField(default=False, verbose_name='Показывать ваш профиль другим пользователям?'),
        ),
    ]