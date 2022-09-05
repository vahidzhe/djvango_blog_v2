from django.shortcuts import render, get_object_or_404
from blog.models import MeqaleModel, KateqoriyaModel
from django.core.paginator import Paginator
from django.views.generic import ListView


class KategoriyaList(ListView):
    template_name = 'pages/kateqoriya.html'
    context_object_name = 'meqaleler'
    paginate_by = 3

    def get_queryset(self):
        kateqoriya = get_object_or_404(
            KateqoriyaModel, slug=self.kwargs['kateqoriyaSlug'])
        return kateqoriya.meqale.order_by('-id')


def kateqoriya(request, kateqoriyaSlug):
    kateqoriya = get_object_or_404(KateqoriyaModel, slug=kateqoriyaSlug)
    meqaleler = kateqoriya.meqale.order_by('-id')
    sehife = request.GET.get('sehife')
    paginator = Paginator(meqaleler, 3)
    context = {
        'meqaleler': paginator.get_page(sehife),
        'kateqoriya_adi': kateqoriya.adi
    }
    return render(request, 'pages/kateqoriya.html', context=context)
