from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index),
   path('user',views.register),
   path('Home',views.Home),
   path('org',views.OrgRegister),
   path('dhoreg',views.DHOregister),
   path('policeofficer',views.policeofficerRegister),
   path('login',views.doLogin),
      path('bookclass/<int:id>',views.bookclass),
 



   path('about',views.About),
   path('logout',views.dologout)

]