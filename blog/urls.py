from django.urls import path
<<<<<<< HEAD
from .views import anasehife, elaqe, kateqoriya, meqalelerim, detay, meqale_yaz, meqale_redakte,meqale_sil,serh_sil
from django.views.generic import TemplateView
=======
from .views import AnaSehife, elaqe, KategoriyaList, meqalelerim, Detay, MeqaleYazCreateView, MeqaleRedakteUpdateView, MeqaleSilDeleteView, serh_sil

>>>>>>> 767b1e6bb5df8d66ac081922a31ed437e067824a

urlpatterns = [
    path('', AnaSehife.as_view(), name='anasehife'),
    path('elaqe', elaqe, name='elaqe'),
    path('kateqoriya/<slug:kateqoriyaSlug>',
         KategoriyaList.as_view(), name='kateqoriya'),
    path('meqalelerim', meqalelerim, name='meqalelerim'),
<<<<<<< HEAD
    path('detay/<slug:slug>', detay, name='detay'),
    path('meqale_yaz', meqale_yaz, name='meqale_yaz'),
    path('meqale_redakte/<slug:slug>', meqale_redakte, name='meqale_redakte'),
    path('meqale_sil/<slug:slug>', meqale_sil, name='meqale_sil'),
    path('serh_sil/<int:id>',serh_sil,name='serh_sil'),
    path('hakkimda', TemplateView.as_view(
        template_name = 'pages/hakkimda.html'
    ), name='hakkimda'),
=======
    path('detay/<slug:slug>', Detay.as_view(), name='detay'),
    path('meqale_yaz', MeqaleYazCreateView.as_view(), name='meqale_yaz'),
    path('meqale_redakte/<slug:slug>',
         MeqaleRedakteUpdateView.as_view(), name='meqale_redakte'),
    path('meqale_sil/<slug:slug>', MeqaleSilDeleteView.as_view(), name='meqale_sil'),
    path('serh_sil/<int:id>',serh_sil,name='serh_sil')
>>>>>>> 767b1e6bb5df8d66ac081922a31ed437e067824a


]
