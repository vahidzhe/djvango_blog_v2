from django import forms
from blog.models import MeqaleModel

class MeqaleRedakteForm(forms.ModelForm):
    class Meta:
        model = MeqaleModel
        exclude = ('yazar','slug')