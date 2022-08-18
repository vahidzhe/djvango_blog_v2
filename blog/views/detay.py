from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from blog.models import MeqaleModel, serh
from .meqalelerim import meqalelerim

def detay(request,slug):
    meqale = get_object_or_404(MeqaleModel,slug = slug)
    serhler =  meqale.serhler.all()
    context = {
        'meqale':meqale,
        'serhler':serhler
    }

    return render(request,'pages/detay.html',context=context)