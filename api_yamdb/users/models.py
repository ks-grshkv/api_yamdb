from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CHOICES = (
        ('admin', 'Администратор'),
        ('user', 'Пользователь'),
        ('moderator', 'Модератор'),
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=10,
        choices=CHOICES,
        default=CHOICES[0],
    )
    # confirmation_code = models.CharField(
    #     max_length=4,
    # )
    # password = None
    username = models.CharField(max_length=40, unique=True)
    # USERNAME_FIELD = 'username'
    email = models.CharField(max_length=40, unique=True)
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
