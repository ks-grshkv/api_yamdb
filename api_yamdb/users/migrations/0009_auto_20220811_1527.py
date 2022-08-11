# Generated by Django 2.2.16 on 2022-08-11 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20220810_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Администратор'), ('moderator', 'Модератор')], default=('user', 'Пользователь'), max_length=10),
        ),
    ]
