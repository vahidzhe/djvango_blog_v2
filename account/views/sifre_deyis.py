from email import message
from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

@login_required(login_url='/')
def sifre_deyis(request):
    form = PasswordChangeForm(request.user,request.POST or None)
    if form.is_valid():
        istifadeci = form.save()
        update_session_auth_hash(request,istifadeci)
        messages.success(request,'Şifrə uğurla dəyiştirildi.')
        return redirect('sifre_deyis')
    context = {
        'form':form,
    }
    return render(request,'pages/sifre_deyis.html',context=context)