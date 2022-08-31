from django.contrib import messages
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from account.forms import ProfilRedakteForm

@login_required(login_url='/')
def profil_redakte(request):
    form = ProfilRedakteForm(request.POST or None,request.FILES or None,instance = request.user)
    if form.is_valid():
        form.save()
        messages.success(request,'Profil Məlumatları redaktə olundu')
        return redirect('profil_redakte')
    context = {
        'form':form,
    }
    return render(request,'pages/profil_redakte.html',context=context)