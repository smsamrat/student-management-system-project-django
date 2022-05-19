from django.shortcuts import render,redirect, HttpResponseRedirect

def HOME(request):
    return render(request,'hod/home.html')