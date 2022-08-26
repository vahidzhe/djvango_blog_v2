from contextlib import redirect_stderr
import imp
from django.shortcuts import render,get_object_or_404,redirect
from blog.models import MeqaleModel
from blog.forms import SerhYazForm

def detay(request,slug):
    meqale = get_object_or_404(MeqaleModel,slug = slug)
    serhler =  meqale.serhler.all()

    serh_form = SerhYazForm(request.POST or None)

    if serh_form.is_valid():
        serh = serh_form.save(commit=False)
        serh.meqale = meqale
        serh.yazar = request.user

        serh.save()
        
        return redirect('detay',slug=slug)

    context = {
        'meqale':meqale,
        'serhler':serhler,
        'serh_form':serh_form
    }

    return render(request,'pages/detay.html',context=context)