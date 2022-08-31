from cmath import log
from django.contrib import messages
from django.shortcuts import redirect,render
from account.forms import QeydiyyatForm
from django.contrib.auth import login,authenticate


def qeydiyyat(request):
    form = QeydiyyatForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username,password=password)
        login(request,user)
        messages.success(request,'Qeydiyyat uğurla olundu')
        return redirect('anasehife')
    context = {
        'form':form,
    }
    return render(request,'pages/qeydiyyat.html',context=context)