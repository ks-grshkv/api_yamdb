# Generated by Django 2.2.16 on 2022-08-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_merge_20220810_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
