from django.urls import path
from .views import cixis


urlpatterns = [
    path('cixis',cixis,name='cixis')
]
