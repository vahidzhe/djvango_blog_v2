from django.urls import path
from .views import AnaSehife, ElaqeFormView, KategoriyaList, meqalelerim, Detay, MeqaleYazCreateView, MeqaleRedakteUpdateView, MeqaleSilDeleteView, serh_sil
from django.views.generic import TemplateView

urlpatterns = [
    path('', AnaSehife.as_view(), name='anasehife'),
    path('elaqe', ElaqeFormView.as_view(), name='elaqe'),
    path('email-gonderildi', TemplateView.as_view(template_name='pages/email_gonderildi.html'), name='email-gonderildi'),
    path('kateqoriya/<slug:kateqoriyaSlug>',KategoriyaList.as_view(), name='kateqoriya'),
    path('meqalelerim', meqalelerim, name='meqalelerim'),
    path('detay/<slug:slug>', Detay.as_view(), name='detay'),
    path('meqale_yaz', MeqaleYazCreateView.as_view(), name='meqale_yaz'),
    path('meqale_redakte/<slug:slug>', MeqaleRedakteUpdateView.as_view(), name='meqale_redakte'),
    path('meqale_sil/<slug:slug>', MeqaleSilDeleteView.as_view(), name='meqale_sil'),
    path('serh_sil/<int:id>',serh_sil,name='serh_sil'),
    path('hakkimda', TemplateView.as_view(
        template_name = 'pages/hakkimda.html'
    ), name='hakkimda'),


]
