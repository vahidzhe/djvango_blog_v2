from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to = 'avatar/',blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'İstifadəçi'
        verbose_name_plural = 'İstifadəçilər'

    def __str__(self):
        return self.username

