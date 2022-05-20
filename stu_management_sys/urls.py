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
    path('hod/home',hod_views.HOME, name='hod_home'),
    path('add-student',hod_views.addStudent, name='add_student')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
