import re
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import SerhModel
from django.contrib import messages

login_required(login_url='/')


def serh_sil(request, id):
    serh = get_object_or_404(SerhModel, id=id)

    if request.user==serh.yazar or request.user==serh.meqale.yazar:
        serh.delete()
        messages.success(request,'Şərh silindi.')
        return redirect('detay',slug=serh.meqale.slug)


    return redirect('meqalelerim')
