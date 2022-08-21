from django.shortcuts import render,redirect
from blog.forms import ElaqeForm
from blog.models import ElaqeModel

def elaqe(request):
    form = ElaqeForm(request.POST or None)
    if form.is_valid():
        elaqe = ElaqeModel()
        elaqe.ad_soyad = form.cleaned_data['ad_soyad']
        elaqe.email = form.cleaned_data['email']
        elaqe.yazi = form.cleaned_data['yazi']
        elaqe.save()
        return redirect('anasehife')



    context = {
        'form':form
    }
    return render(request,'pages/elaqe.html',context=context)