from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app.models import CustomUser,Course,SessionYear

@login_required(login_url='/')
def HOME(request):
    return render(request,'hod/home.html')

@login_required(login_url='/')
def addStudent(request):
    course = Course.objects.all()
    session_year = SessionYear.objects.all()
    print(session_year)
    context ={
        'course':course,
        'session_year':session_year,
    }

    return render(request,'hod/add_student.html',context)