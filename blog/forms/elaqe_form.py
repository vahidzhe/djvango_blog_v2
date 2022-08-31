from dataclasses import fields
from pyexpat import model
from django import forms
from blog.models import ElaqeModel


class ElaqeForm(forms.ModelForm):
    class Meta:
        model = ElaqeModel
        fields = ('ad_soyad','email','yazi')
