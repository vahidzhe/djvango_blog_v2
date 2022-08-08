from abc import abstractmethod
from operator import mod
from django.db import models

class DateAbstractModel(models.Model):
    yaranma_tarixi = models.DateTimeField(auto_now_add=True)
    redakte_tarixi = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True