from django.shortcuts import render,get_object_or_404
from blog.models import MeqaleModel,KateqoriyaModel
from django.core.paginator import Paginator

def kateqoriya(request,kateqoriyaSlug):
    kateqoriya = get_object_or_404(KateqoriyaModel,slug = kateqoriyaSlug)
    meqaleler = kateqoriya.meqale.order_by('-id')
    sehife = request.GET.get('sehife')
    paginator  = Paginator(meqaleler,3)
    context = {
        'meqaleler':paginator.get_page(sehife),
        'kateqoriya_adi':kateqoriya.adi
    }
    return render(request,'pages/kateqoriya.html',context=context)