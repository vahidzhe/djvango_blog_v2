from django.urls import reverse,reverse_lazy
from django.shortcuts import get_object_or_404
from blog.models import MeqaleModel
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin



class MeqaleRedakteUpdateView(UpdateView,LoginRequiredMixin):
    login_url = reverse_lazy('giris')
    template_name = 'pages/meqale_redakte.html'
    fields = ('basliq', 'kateqoriya', 'yazi', 'sekil')

    def get_object(self):
        meqale = get_object_or_404(
            MeqaleModel, slug=self.kwargs.get('slug'), yazar=self.request.user)
        return meqale

    def get_success_url(self):
        return reverse('detay', kwargs={'slug': self.get_object().slug})


