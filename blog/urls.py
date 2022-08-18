from django.urls import path
from .views import anasehife,elaqe,kateqoriya,meqalelerim,detay


urlpatterns = [
    path('', anasehife,name='anasehife'),
    path('elaqe', elaqe,name='elaqe'),
    path('kateqoriya/<slug:kateqoriyaSlug>', kateqoriya,name='kateqoriya'),
    path('meqalelerim',meqalelerim,name='meqalelerim'),
    path('detay/<slug:slug>', detay,name='detay'),
    
]
