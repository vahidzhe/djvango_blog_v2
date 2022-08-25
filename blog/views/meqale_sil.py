from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import MeqaleModel

login_required(login_url='/')
def meqale_sil(request, slug):
    get_object_or_404(MeqaleModel, slug=slug).delete()

    return redirect('meqalelerim')
