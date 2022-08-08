from statistics import mode
from tabnanny import verbose
from django.db import models

class ElaqeModel(models.Model):
    email = models.EmailField(max_length=250)
    ad_soyad = models.CharField(max_length=150)
    yazi = models.TextField()
    yaranma_tarixi = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'elaqe'
        verbose_name = 'Əlaqə'
        verbose_name_plural = 'Əlaqə'

    def __str__(self):
        return self.ad_soyad