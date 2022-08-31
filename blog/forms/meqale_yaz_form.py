from django import forms
from blog.models import MeqaleModel

class MeqaleYazForm(forms.ModelForm):
    class Meta:
        model = MeqaleModel
        exclude = ('yazar','slug')