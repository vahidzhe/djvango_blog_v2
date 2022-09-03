from django.urls import path
from .views import AnaSehife, elaqe, kateqoriya, meqalelerim, Detay, meqale_yaz, meqale_redakte,meqale_sil,serh_sil


urlpatterns = [
    path('', AnaSehife.as_view(), name='anasehife'),
    path('elaqe', elaqe, name='elaqe'),
    path('kateqoriya/<slug:kateqoriyaSlug>', kateqoriya, name='kateqoriya'),
    path('meqalelerim', meqalelerim, name='meqalelerim'),
    path('detay/<slug:slug>', Detay.as_view(), name='detay'),
    path('meqale_yaz', meqale_yaz, name='meqale_yaz'),
    path('meqale_redakte/<slug:slug>', meqale_redakte, name='meqale_redakte'),
    path('meqale_sil/<slug:slug>', meqale_sil, name='meqale_sil'),
    path('serh_sil/<int:id>',serh_sil,name='serh_sil')


]
