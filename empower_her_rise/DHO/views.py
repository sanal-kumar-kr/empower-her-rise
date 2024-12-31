from django.shortcuts import render
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . forms import *

# Create your views here.
def addschema(request):
    form = SchemasForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.userid=request.user
            data.save()
            messages.success(request, f'Schema Added Succesfully', extra_tags='user_reg')
            return redirect('/viewschema')
    else:
        form = SchemasForm()
    return render(request,'register.html',{'form':form,'title':'Add Schemas'})

def viewschema(request):
    if request.user.usertype == 0:
        data=Schemas.objects.all()
    else:
       data=Schemas.objects.filter(userid=request.user.id)
    return render(request,'view_schemas.html',{'data':data})


def editschema(request,id):
    data=Schemas.objects.get(id=id)
    form = SchemasForm(request.POST,request.FILES,instance=data)
    if request.method=='POST':
        if form.is_valid():
            data.save()
            messages.success(request, f'Schema Edited Succesfully', extra_tags='user_reg')
            return redirect('/viewschema')
    else:
        form = SchemasForm(instance=data)
    return render(request,'register.html',{'form':form,'title':'Edit Schema'})


def addcheckup(request):
    form = healthcheckupForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.userid=request.user
            data.save()
            messages.success(request, f'checkup Added Succesfully', extra_tags='user_reg')
            return redirect('/viewcheckup')
    else:
        form = healthcheckupForm()
    return render(request,'register.html',{'form':form,'title':'Add checkup','checkup':True})



def viewcheckup(request):
    if request.user.usertype == 0:
        data=healthcheckup.objects.all()
    else:
       data=healthcheckup.objects.filter(userid=request.user.id)
    return render(request,'view_healthcheckup.html',{'data':data})
    


def editcheckup(request,id):
    data=healthcheckup.objects.get(id=id)
    form = healthcheckupForm(request.POST,request.FILES,instance=data)
    if request.method=='POST':
        if form.is_valid():
            data.save()
            messages.success(request, f'checkup Edited Succesfully', extra_tags='user_reg')
            return redirect('/viewcheckup')
    else:
        form = healthcheckupForm(instance=data)
    return render(request,'register.html',{'form':form,'title':'Edit checkup','checkup':True})


def deletecheckup(request,id):
    data=healthcheckup.objects.get(id=id)
    data.delete()
    messages.success(request, f'checkup Deleted', extra_tags='user_reg')
    return redirect('/viewcheckup')

def deleteschema(request,id):
    data=Schemas.objects.get(id=id)
    data.delete()
    messages.success(request, f'schema Deleted', extra_tags='user_reg')

    return redirect('/viewschema')

def view_more_schema(request,id):
    data=Schemas.objects.get(id=id)
    return render(request,'view_more_schema.html',{'data':data})



