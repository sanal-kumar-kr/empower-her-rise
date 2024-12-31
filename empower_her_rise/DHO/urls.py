from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
   path('addschema',views.addschema),
   path('viewschema',views.viewschema),
    path('deleteschema/<int:id>',views.deleteschema),
   path('editschema/<int:id>',views.editschema),

   path('addcheckup',views.addcheckup),
   path('viewcheckup',views.viewcheckup),
    path('deletecheckup/<int:id>',views.deletecheckup),
   path('editcheckup/<int:id>',views.editcheckup),
   path('view_more_schema/<int:id>',views.view_more_schema),


]