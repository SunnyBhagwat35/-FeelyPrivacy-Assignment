from django.db import models
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        if not username:
            raise ValueError('The Username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    user_mobile = models.IntegerField(null=True)
    is_emp = models.BooleanField(verbose_name="employee", default=False, )
    is_manager = models.BooleanField(verbose_name="manager", default=False, )
    objects = UserManager()

    class Meta:
        verbose_name_plural = 'ACCOUNTS'

    def _str_(self):
        return self.username


class Schedule(models.Model):
    time = models.DateTimeField()
    booked = models.BooleanField(default=False)
    def __str__(self):
        return str(self.time)