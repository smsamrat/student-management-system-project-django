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

    #hod
    path('hod/home',hod_views.HOME, name='hod_home')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
