from django.shortcuts import render, redirect
from blog.forms import MeqaleYazForm
from blog.models import MeqaleModel
from django.contrib.auth.decorators import login_required


login_required(login_url='/')


def meqale_yaz(request):
    form = MeqaleYazForm(request.POST or None, files=request.FILES or None)

    if form.is_valid():
        meqale = form.save(commit=False)
        meqale.yazar = request.user
        meqale.save()
        form.save_m2m()
        
        return redirect('detay',slug=meqale.slug)


    context = {
        'form': form
    }
    return render(request, 'pages/meqale_yaz.html', context=context)
