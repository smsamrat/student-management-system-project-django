from django.contrib import messages
from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app.models import CustomUser,Course,SessionYear,Student

@login_required(login_url='/')
def HOME(request):
    return render(request,'hod/home.html')

@login_required(login_url='/')
def addStudent(request):
    course = Course.objects.all()
    session_year = SessionYear.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        session_year_id = request.POST.get('session_year_id')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Already Exist')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Already Exist')
            return redirect('add_student')
        else:
            user =CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)
            session_year = SessionYear.objects.get(id = session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_student')

    context ={
        'course':course,
        'session_year':session_year,
    }

    return render(request,'hod/add_student.html',context)

@login_required(login_url='/')
def viewStudent(request):
    student = Student.objects.all().order_by("-id")
    context ={
        'student':student
    }
    return render(request,'hod/student_view.html',context)

@login_required(login_url='/')
def editStudent(request, id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = SessionYear.objects.all()
    print(student)
    context ={
        'student':student,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'hod/edit_student.html',context)