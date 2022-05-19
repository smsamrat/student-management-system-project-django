
from django.shortcuts import redirect, render,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from app.models import CustomUser
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required



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

@login_required(login_url='/')
def doLogout(request):
    logout(request)
    return redirect('login')    

@login_required(login_url='/')    
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    print(user)

    context ={
        'user':user,
    }

    return render(request,'profile.html',context)

@login_required(login_url='/') 
def updateProfile(request):
    if request.method =="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        print(profile_pic)
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if password !=None and password != "":
                customuser.set_password(password)
                
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic

            customuser.save()
            messages.success(request,'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.warning(request,'Your Profile Updated Failed !')
    return render(request,'profile.html')