
from django.shortcuts import redirect, render,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages


def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request, 
        username=request.POST.get('Email'),
        password=request.POST.get('Password'))
        if user!= None:
            login(request,user)
            user_type =user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return HttpResponse('Stuff')
            elif user_type == '1':
                return HttpResponse('Student')
            else:
                messages.warning(request,'Email and Password Are Invalid !')
                return redirect('login')
        else:
            messages.warning(request,'Email and Password Are Invalid !')
            return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')          