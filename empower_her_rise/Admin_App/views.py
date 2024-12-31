from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . forms import *
from itertools import chain
from django.utils import timezone
from django.db.models import Q

# Create your views here.
def users(request):
   
    user=Register.objects.filter(usertype=0)
    org = Register.objects.filter(usertype=2).filter(Q(status=0) | Q(status=1) | Q(status=2) | Q(status=3))
    police=Register.objects.filter(usertype=4)
    dho=Register.objects.filter(usertype=3)
    return render(request,'view_user_requests.html',{'user':user,'org':org,'police':police,'dho':dho})


def addtalentgroupes(request):
    form = TalentgroupForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            form.save()
          
            messages.success(request, f'Added SuccessFully', extra_tags='user_reg')
            return redirect('/viewtalentgroupes')
    else:
        form = TalentgroupForm()
    return render(request,'register.html',{'form':form,'title':'Add Talent Groupes'})

def edittalentgroupes(request,id):
    data=Talentgroup.objects.get(id=id)
    form = TalentgroupForm(request.POST,request.FILES,instance=data)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Group Edited', extra_tags='user_reg')
            return redirect('/viewtalentgroupes')
    else:
        form = TalentgroupForm(instance=data)
    return render(request,'register.html',{'form':form,'title':'Edit Talent Groupes'})


def viewtalentgroupes(request):
    data=Talentgroup.objects.all()
    return render(request,'view_talentgroupes.html',{'data':data})

def joingroup(request,id):
    if request.user.usertype == 0:
        uni=members.objects.filter(userid=request.user,gpid=id).first()
        if uni:
            messages.success(request, f'Already Joined', extra_tags='user_reg')

            return redirect('/viewtalentgroupes')
    members.objects.create(
        userid=request.user,
        gpid=Talentgroup.objects.get(id=id),
    )
    messages.success(request, f' Joined Successfully', extra_tags='user_reg')

    return redirect('/viewtalentgroupes')


def deletetalentgroup(request,id):
    data=Talentgroup.objects.get(id=id)
    data.delete()
    messages.success(request, f'Group Deleted', extra_tags='user_reg')

    return redirect('/viewtalentgroupes')
def addclassess(request):
    form = classesForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.userid=request.user
            data.save()
            messages.success(request, f'class Added Successfully', extra_tags='user_reg')
            return redirect('/viewclasses')
    else:
        form = classesForm()
    return render(request,'register.html',{'form':form,'title':'Add Classes','Time':True,'checkup':True})


def addvideo(request,id):
    form = videoform(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.classid=classes.objects.get(id=id)
            data.save()
            messages.success(request, f'Video Added Successfully', extra_tags='user_reg')
            return redirect('/viewclasses')
    else:
        form = videoform()
    return render(request,'register.html',{'form':form,'title':'Add Video'})


def viewvideo(request,id):
    user=classes.objects.get(id=id)
    if request.user.usertype == 0 and user.userid.usertype == 2 :
        book=booking.objects.filter(user=request.user.id,classid=id).first()
        if not book:
            messages.success(request, f'YOu Are not Booked Class un available', extra_tags='user_reg')
            return redirect('/viewclasses')

    data=classvideo.objects.filter(classid=id)
    print(data)
    return render(request,'view_video.html',{'data':data})









def viewclasses(request):
    query = request.GET.get('q')
    if request.user.usertype == 0:
        if query:
            data = classes.objects.filter(title__icontains=query)
        else:
            data = classes.objects.all()
    else:
        if query:
            data = classes.objects.filter(userid=request.user.id, title__icontains=query)
        else:
            data = classes.objects.filter(userid=request.user.id)
    return render(request, 'view_classes.html', {'data': data})


def member(request,id):
    if request.user.usertype == 0:
        uni=   members.objects.filter(userid=request.user,gpid=id).first()
        if not uni:
            messages.success(request, f'First You Should Join The Group', extra_tags='user_reg')
            return redirect('/viewtalentgroupes')

    data=members.objects.filter(gpid=id)
    return render(request,'view_members.html',{'data':data})


def approve(request,id):
    data=Register.objects.get(id=id)
    data.status=1
    data.save()
    return redirect('/users')


def reject(request,id):
    data=Register.objects.get(id=id)
    data.status=2
    data.save()
    return redirect('/users')


def disable(request,id):
    data=Register.objects.get(id=id)
    data.status=3
    data.save()
    return redirect('/users')


def enable(request,id):
    data=Register.objects.get(id=id)
    data.status=1
    data.save()
    return redirect('/users')


def editclasses(request,id):
    data=classes.objects.get(id=id)
    form = classesForm(request.POST,request.FILES,instance=data)
    if request.method=='POST':
        if form.is_valid():
           
            form.save()
            messages.success(request, f'class Added Successfully', extra_tags='user_reg')
            return redirect('/viewclasses')
    else:
        form = classesForm(instance=data)
    return render(request,'register.html',{'form':form,'title':'Add Classes'})



def deleteclass(request,id):
    data=classes.objects.get(id=id)
    data.delete()
    messages.success(request, f'class deleted Successfully', extra_tags='user_reg')

    return redirect('/viewclasses')

def chat(request):
    if request.user.usertype == 0:
        data = Register.objects.filter(usertype__in=[3,4],status=1)
    else:
       data=Register.objects.filter(usertype=0)
    return render(request,'chat_index.html',{'data':data})



def message(request,id):
     
    if request.method=='POST':
        form = messageform(request.POST,request.FILES)
       
        if form.is_valid():
            print("valid")
            
            inbox.objects.create(
                sender =Register.objects.get(id=request.user.id),
                reciever = Register.objects.get(id=id),
                message = form.cleaned_data["message"],
                datetime=timezone.now()
                )
          
            data1=inbox.objects.filter(sender=request.user.id,reciever=id)
            data2=inbox.objects.filter(sender=id,reciever=request.user.id)
            merged_data = list(chain(data1, data2))
            merged_data.sort(key=lambda x: x.datetime) 
            return render(request,'chat_interface.html',{'data':merged_data,'form':form})
    else:
        form = messageform()
        data1=inbox.objects.filter(sender=request.user.id,reciever=id)
        data2=inbox.objects.filter(sender=id,reciever=request.user.id)
        merged_data = list(chain(data1, data2))
        merged_data.sort(key=lambda x: x.datetime) 
        print(merged_data)
    return render(request,'chat_interface.html',{'form':form,'data':merged_data})


def bookings(request,id):
    if request.user.usertype == 0:
        data=booking.objects.filter(user=id)
        return render(request,'my_bookings.html',{'data':data})
    else:    
        data=booking.objects.filter(classid=id)
        return render(request,'view_bookings.html',{'data':data})


def cancelbooking(request,id):
    data=booking.objects.get(id=id)
    data.delete()
    messages.success(request, f'Booking Cancelled Successfully', extra_tags='user_reg')
    return redirect('/viewclasses')



def addfeedback(request,id):
    form = feedbackform(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.userid=request.user
            data.classid=classes.objects.get(id=id)
            data.save()
            messages.success(request, f'Feedback Added Successfully', extra_tags='user_reg')
            return redirect('/viewclasses')
    else:
        form = feedbackform()
    return render(request,'register.html',{'form':form,'title':'Add Feedback'})


def viewfeedback(request,id):
        data=feedback.objects.filter(classid=id)
        return render(request,'view_feedback.html',{'data':data})


def replyfeedback(request,id):
    form = replyform(request.POST,request.FILES)
    data=feedback.objects.get(id=id)
    if request.method=='POST':
        if form.is_valid():
            data.reply=form.cleaned_data['reply']
            data.save()
            messages.success(request, f'Replied Successfully', extra_tags='user_reg')
            return redirect('/viewclasses')
    else:
        form = replyform()
    return render(request,'register.html',{'form':form,'title':'Reply Feedback'})



def chatgroup(request,id):
    if request.method=='POST':
        form = groupchatform(request.POST,request.FILES)
        if form.is_valid():
            groupinbox.objects.create(
                sender =Register.objects.get(id=request.user.id),
                groupid =Talentgroup.objects.get(id=id),
                message = form.cleaned_data["message"],
                datetime=timezone.now()
                )
            data=groupinbox.objects.filter(groupid=id)
            return render(request,'chatgroup.html',{'data':data,'form':form})
    else:
        form = groupchatform()
        data=groupinbox.objects.filter(groupid=id)
        if request.user.usertype == 0:

            uni=   members.objects.filter(userid=request.user,gpid=id).first()
            if not uni:
                messages.success(request, f'First You Should Join The Group', extra_tags='user_reg')
                return redirect('/viewtalentgroupes')

    return render(request,'chatgroup.html',{'form':form,'data':data})



def deletechat(request,id):
    data=inbox.objects.get(id=id)
    data.delete()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or '/')

def deletegroupchat(request,id):
    data=groupinbox.objects.get(id=id)
    data.delete()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or '/')


def deleteclassvideo(request,id):
    data=classvideo.objects.get(id=id)
    data.delete()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or '/')