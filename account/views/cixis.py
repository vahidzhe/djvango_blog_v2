from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def cixis(request):
    logout(request)
    messages.success(request,'Hesabdan çıxış edildi')
    return redirect('anasehife')
