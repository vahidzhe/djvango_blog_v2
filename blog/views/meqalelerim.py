from django.shortcuts import render,get_object_or_404
from blog.models import MeqaleModel,KateqoriyaModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def meqalelerim(request):
    meqaleler = request.user.meqaleler.order_by('-id')
    
    sehife = request.GET.get('sehife')
    paginator  = Paginator(meqaleler,10)
    context = {
        'meqaleler':paginator.get_page(sehife),
        
    }
    return render(request,'pages/meqalelerim.html',context=context)