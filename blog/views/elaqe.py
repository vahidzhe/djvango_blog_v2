from django.shortcuts import render, redirect
from blog.forms import ElaqeForm
from blog.models import ElaqeModel


def elaqe(request):
    form = ElaqeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('anasehife')

    context = {
        'form': form
    }
    return render(request, 'pages/elaqe.html', context=context)
