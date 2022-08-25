from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import MeqaleRedakteForm
from blog.models import MeqaleModel
from django.contrib.auth.decorators import login_required


login_required(login_url='/')


def meqale_redakte(request, slug):
    meqale = get_object_or_404(MeqaleModel, slug=slug)
    
    form = MeqaleRedakteForm(request.POST or None,
                             request.FILES or None, instance=meqale)


    if form.is_valid():
        form.save()
        return redirect('detay', slug=meqale.slug)

    context = {
        'form': form
    }
    return render(request, 'pages/meqale_redakte.html', context=context)
