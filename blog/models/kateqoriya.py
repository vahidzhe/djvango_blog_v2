from enum import unique
from operator import mod
from tabnanny import verbose
from django.db import models
from autoslug import AutoSlugField

class KateqoriyaModel(models.Model):
    adi = models.CharField(max_length=30,blank=False, null=False)
    slug = AutoSlugField(populate_from = 'adi',unique = True)

    class Meta:
        db_table = 'kateqoriya'
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def __str__(self):
        return self.adi