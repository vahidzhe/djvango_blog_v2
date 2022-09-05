from django.shortcuts import render, redirect
from blog.forms import ElaqeForm
from blog.models import ElaqeModel
from django.views.generic import FormView

class ElaqeFormView(FormView):
    form_class = ElaqeForm
    template_name = 'pages/elaqe.html'
    success_url = '/elaqe/email-gonderildi'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def elaqe(request):
    form = ElaqeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('anasehife')

    context = {
        'form': form
    }
    return render(request, 'pages/elaqe.html', context=context)
