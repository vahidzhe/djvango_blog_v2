from django.urls import path
from .views import anasehife, elaqe, kateqoriya, meqalelerim, detay, meqale_yaz, meqale_redakte,meqale_sil


urlpatterns = [
    path('', anasehife, name='anasehife'),
    path('elaqe', elaqe, name='elaqe'),
    path('kateqoriya/<slug:kateqoriyaSlug>', kateqoriya, name='kateqoriya'),
    path('meqalelerim', meqalelerim, name='meqalelerim'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('meqale_yaz', meqale_yaz, name='meqale_yaz'),
    path('meqale_redakte/<slug:slug>', meqale_redakte, name='meqale_redakte'),
    path('meqale_sil/<slug:slug>', meqale_sil, name='meqale_sil'),


]
