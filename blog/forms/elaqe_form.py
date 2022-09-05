from dataclasses import fields
from pyexpat import model
from django import forms
from blog.models import ElaqeModel
from django.core.mail import send_mail


class ElaqeForm(forms.ModelForm):
    class Meta:
        model = ElaqeModel
        fields = ('ad_soyad','email','yazi')

    def email_gonder(self,mesaj):
        send_mail(
            subject = 'Elaqe formundan yeni mesaj var!',
            message=mesaj,
            from_email= None,
            recipient_list=['gasanzadeh99(@gmail.com','vahidzhe@gmail.com'],
            fail_silently=False

        )
