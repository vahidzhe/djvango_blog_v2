from django.db import models
from blog.models import KateqoriyaModel
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from blog.models.abstract_models import DateAbstractModel


class MeqaleModel(DateAbstractModel):
    basliq = models.CharField(max_length=50)
    kateqoriya = models.ManyToManyField(KateqoriyaModel, related_name='meqale')
    yazi = RichTextField()
    sekil = models.ImageField(upload_to='meqale_sekilleri')
    yazar = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE,
                              related_name='meqaleler')
    slug = AutoSlugField(populate_from='basliq')

    class Meta:
        db_table = 'meqale'
        verbose_name = 'Məqalə'
        verbose_name_plural = 'Məqalələr'

    def __str__(self):
        return self.basliq
