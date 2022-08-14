from django.urls import path
from .views import index,elaqe


urlpatterns = [
    path('', index),
    path('elaqe', elaqe),
    
]
