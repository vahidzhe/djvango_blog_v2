from curses.ascii import CR
from django.shortcuts import render, redirect
from blog.forms import MeqaleYazForm
from blog.models import MeqaleModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse


class MeqaleYazCreateView(CreateView):
    template_name = 'pages/meqale_yaz.html'
    model = MeqaleModel
    fields = ('basliq', 'kateqoriya', 'yazi', 'sekil')

    def get_success_url(self):
        return reverse('detay', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        meqale = form.save(commit=False)
        meqale.yazar = self.request.user
        meqale.save()
        form.save_m2m()

        return super().form_valid(form)
