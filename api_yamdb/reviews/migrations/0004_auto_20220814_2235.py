# Generated by Django 2.2.16 on 2022-08-14 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220814_2234'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='unique_booking',
        ),
    ]