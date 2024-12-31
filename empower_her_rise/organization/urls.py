from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
   path('addhostals',views.addhostal),
   path('viewhostals',views.viewhostal),
    path('edithostal/<int:id>',views.edithostal),
    path('addcourses',views.addcources),
    path('viewcourses',views.viewcources),
    path('editcourses/<int:id>',views.editcourses),
    path('enrolledusers/<int:id>',views.enrolledusers),
    path('addjobs',views.addjobs),
    path('viewjobs',views.viewjobs),
    path('editjobs/<int:id>',views.editjobs),
    path('enrollcources/<int:id>',views.enrollcources),
    path('uploadcerti/<int:id>',views.uploadcerti),
    path('viewmorehostal/<int:id>',views.viewmorehostal),
    path('addhostalfeedback/<int:id>',views.addhostalfeedback),
    path('addcourcevideo/<int:id>',views.addcourcevideo),
    path('addlink/<int:id>',views.addlink),
    path('viewmorecourse/<int:id>',views.viewmorecourse),
    path('deletehostalfeedback/<int:id>',views.deletehostalfeedback),
    path('deletecourselink/<int:id>',views.deletecourselink),
    path('deletecoursevideo/<int:id>',views.deletecoursevideo),
    path('viewmorejobs/<int:id>',views.viewmorejobs)


]