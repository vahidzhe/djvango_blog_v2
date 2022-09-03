from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import MeqaleModel
from django.views.generic import DeleteView
from django.urls import reverse_lazy


class MeqaleDelete(DeleteView):
    template_name = 'pages/meqale_sil.html'
    context_object_name = 'meqale'
    success_url = reverse_lazy('meqalelerim')

    def get_queryset(self):
        meqale = MeqaleModel.objects.filter(slug = self.kwargs['slug'],yazar = self.request.user)
        return  meqale


login_required(login_url='/')
def meqale_sil(request, slug):
    get_object_or_404(MeqaleModel, slug=slug).delete()

    return redirect('meqalelerim')
