from django import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import hod_views,stuff_views,stu_views, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE, name='base'),

    #login
    path('',views.LOGIN, name='login'),
    path('login/',views.doLogin, name='doLogin'),

    #logout
    path('logout/',views.doLogout, name='doLogout'),

    #profile
    path('profile/',views.PROFILE, name='profile'),
    path('update-profile/',views.updateProfile, name='update_profile'),

    #hod
    #add student

    path('hod/home',hod_views.HOME, name='hod_home'),
    path('add-student',hod_views.addStudent, name='add_student'),
    path('view-student',hod_views.viewStudent, name='view_student'),
    path('edit-student/<str:id>',hod_views.editStudent, name='edit_student'),
    path('update-student/',hod_views.updateStudent, name='update_student'),
    path('delete-student/<str:admin>',hod_views.deleteStudent, name='delete_student'),

    #add course
    path('hod/add-course', hod_views.addCourse, name='add_course'),
    path('hod/view-course', hod_views.viewCourse, name='view_course'),
    path('hod/edit-course/<str:id>', hod_views.editCourse, name='edit_course'),
    path('hod/update-course', hod_views.updateCourse, name='update_course'),
    path('hod/delete-course/<str:id>', hod_views.deleteCourse, name='delete_course'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
