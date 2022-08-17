from django.shortcuts import render
from blog.models import MeqaleModel
from django.core.paginator import Paginator
from django.db.models import Q

def anasehife(request):
    sorgu = request.GET.get('sorgu')
    meqaleler = MeqaleModel.objects.order_by('-id')
    if sorgu:
        meqaleler = meqaleler.filter(
            Q(basliq__icontains = sorgu)  | Q(yazi__icontains = sorgu)
        ).distinct()
    sehife = request.GET.get('sehife')
    paginator  = Paginator(meqaleler,3)
    context = {
        'meqaleler':paginator.get_page(sehife)
    }
    return render(request,'pages/anasehife.html',context=context)