from django.shortcuts import render, redirect
from blog.forms import ElaqeForm
from blog.models import ElaqeModel
from django.views.generic import FormView

class ElaqeFormView(FormView):
    form_class = ElaqeForm
    template_name = 'pages/elaqe.html'
    success_url = 'email-gonderildi'

    def form_valid(self, form):
        form.save()
        form.email_gonder(
            mesaj = form.cleaned_data['yazi']
        )
        return super().form_valid(form)

