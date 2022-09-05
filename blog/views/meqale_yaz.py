from blog.models import MeqaleModel
from django.views.generic import CreateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class MeqaleYazCreateView(CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('giris')
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
