from django import forms
from blog.models import SerhModel


class SerhYazForm(forms.ModelForm):
    class Meta:
        model = SerhModel
        fields = ('yazi',)