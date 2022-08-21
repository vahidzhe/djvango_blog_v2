from django import forms


class ElaqeForm(forms.Form):
    email = forms.EmailField(max_length=100, label='E-Mail',widget=forms.EmailInput(attrs={'class':'form-control'}))
    ad_soyad = forms.CharField(max_length=50,label='Ad Soyad',widget=forms.TextInput(attrs={'class':'form-control'}))
    yazi = forms.CharField(label='Yazı',widget=forms.Textarea(
        attrs={'class': 'form-control','rows' : 5}))
