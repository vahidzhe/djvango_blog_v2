from re import template
from django.urls import path
from .views import cixis,sifre_deyis,profil_redakte,qeydiyyat
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('cixis',cixis,name='cixis'),
    path('sifre_deyis', sifre_deyis, name='sifre_deyis'),
    path('profil_redakte', profil_redakte, name='profil_redakte'),
    path('qeydiyyat', qeydiyyat, name='qeydiyyat'),
    path('giris', LoginView.as_view(
        template_name='pages/giris.html'
        ), name='giris'),
]
