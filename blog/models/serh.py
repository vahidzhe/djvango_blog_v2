from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from .meqale import MeqaleModel


class SerhModel(models.Model):
    yazar = models.ForeignKey(
        'account.CustomUserModel', on_delete=models.CASCADE, related_name='serhler')
    yazi = models.TextField()

    meqale = models.ForeignKey(
        MeqaleModel, on_delete=models.CASCADE, related_name='serhler')
    yaranma_tarixi = models.DateTimeField(auto_now_add=True)
    redakte_tarixi = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'serh'
        verbose_name = 'Şərh'
        verbose_name_plural = 'Şərhlər'

    def __str__(self):
        return self.yazar.username