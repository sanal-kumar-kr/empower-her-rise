from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('addtalentgroupes',views.addtalentgroupes),
    path('viewtalentgroupes',views.viewtalentgroupes),
    path('addclassess',views.addclassess),
    path('viewclasses',views.viewclasses),
    path('users',views.users),
    path('chat',views.chat),
    path('approve/<int:id>',views.approve),
    path('reject/<int:id>',views.reject),
    path('disable/<int:id>',views.disable),
    path('enable/<int:id>',views.enable),
    path('message/<int:id>',views.message),
    path('members/<int:id>',views.member),
    path('joingroup/<int:id>',views.joingroup),
    path('editclasses/<int:id>',views.editclasses),
    path('deleteclass/<int:id>',views.deleteclass),
    path('addvideo/<int:id>',views.addvideo),
    path('viewvideo/<int:id>',views.viewvideo),
    path('bookings/<int:id>',views.bookings),
    path('cancelbooking/<int:id>',views.cancelbooking),
    path('addfeedback/<int:id>',views.addfeedback),
    path('viewfeedback/<int:id>',views.viewfeedback),
    path('replyfeedback/<int:id>',views.replyfeedback),
    path('edittalentgroupes/<int:id>',views.edittalentgroupes),
    path('deletetalentgroup/<int:id>',views.deletetalentgroup),
    path('chatgroup/<int:id>',views.chatgroup),
    path('deletechat/<int:id>',views.deletechat),
    path('deletegroupchat/<int:id>',views.deletegroupchat),
    path('deleteclassvideo/<int:id>',views.deleteclassvideo),


]