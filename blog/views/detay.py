from django.shortcuts import render, get_object_or_404, redirect
from blog.models import MeqaleModel
from blog.forms import SerhYazForm
from django.views import View
import logging

logger = logging.getLogger('konu_okuma')


class Detay(View):
    http_method_names = ['get', 'post']
    serh_form = SerhYazForm

    def get(self, request, slug):
        meqale = get_object_or_404(MeqaleModel, slug=slug)
        serhler = meqale.serhler.order_by('-id')
        if request.user.is_authenticated:
            logger.info('')
        context = {
            'meqale': meqale,
            'serhler': serhler,
            'serh_form': self.serh_form()
        }

        return render(request, 'pages/detay.html', context=context)

    def post(self, request, slug):
        meqale = get_object_or_404(MeqaleModel, slug=slug)
        serh_form = self.serh_form(request.POST)
        if serh_form.is_valid():
            serh = serh_form.save(commit=False)
            serh.meqale = meqale
            serh.yazar = request.user
            serh.save()
            return redirect('detay', slug=slug)
