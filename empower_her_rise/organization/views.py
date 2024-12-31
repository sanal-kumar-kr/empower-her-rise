from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . forms import *
from .models import *
from authentication.forms import *
from django.db.models import Avg
from django.utils import timezone
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def addcources(request):
    form = CorceForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.userid=request.user
            data.save()
            messages.success(request, f'cource Added Successfully', extra_tags='user_reg')
            return redirect('/viewcourses')
    else:
        form = CorceForm()
    return render(request,'register.html',{'form':form,'title':'Add cource'})

def viewcources(request):
    query = request.GET.get('q')
    if request.user.usertype == 0:
        if query:
            data = courses.objects.filter(title__icontains=query)
        else:
            data = courses.objects.all()
    else:
        if query:
            data = courses.objects.filter(userid=request.user.id, title__icontains=query)
        else:
            data = courses.objects.filter(userid=request.user.id)
    return render(request, 'view_corces.html', {'data': data})

def editcourses(request,id):
    data=courses.objects.get(id=id)
    form = CorceForm(request.POST,request.FILES,instance=data)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Cource Edited Successfully', extra_tags='user_reg')
            return redirect('/viewcourses')
    else:
        form = CorceForm(instance=data)
    return render(request,'register.html',{'form':form,'title':'Edit courses'})



def addhostal(request):
    form = hostalForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.userid=request.user
            data.save()
            messages.success(request, f'Hostal Added Successfully', extra_tags='user_reg')
            return redirect('/viewhostals')
    else:
        form = hostalForm()
    return render(request,'register.html',{'form':form,'title':'Add Hostal'})

# def viewhostal(request):
#     if request.user.usertype == 0:
#         data=hostals.objects.all()
#     else:
#        data=hostals.objects.filter(userid=request.user.id)
#     return render(request,'view_hostals.html',{'data':data})



def viewhostal(request):
    query = request.GET.get('q')
    if request.user.usertype == 0:
        if query:
            data = hostals.objects.filter(hostal_name__icontains=query).annotate(avg_rating=Avg('oirtryguhijofrewgfrewuketerwtwop__ratings'))
        else:
            data = hostals.objects.all().annotate(avg_rating=Avg('oirtryguhijofrewgfrewuketerwtwop__ratings'))
    else:
        if query:
            data = hostals.objects.filter(userid=request.user.id, hostal_name__icontains=query).annotate(avg_rating=Avg('oirtryguhijofrewgfrewuketerwtwop__ratings'))
        else:
            data = hostals.objects.filter(userid=request.user.id).annotate(avg_rating=Avg('oirtryguhijofrewgfrewuketerwtwop__ratings'))
    return render(request, 'view_hostals.html', {'data': data})



def edithostal(request,id):
    data=hostals.objects.get(id=id)
    form = hostalForm(request.POST,request.FILES,instance=data)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Hostal Edited Successfully', extra_tags='user_reg')
            return redirect('/viewhostals')
    else:
        form = hostalForm(instance=data)
    return render(request,'register.html',{'form':form,'title':'Edit Hostal'})


def addjobs(request):
    form = JobForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.userid=request.user
            data.save()
            messages.success(request, f'Job Added Successfully', extra_tags='user_reg')
            return redirect('/viewjobs')
    else:
        form = JobForm()
    return render(request,'register.html',{'form':form,'title':'Add Job'})

def viewjobs(request):
    query = request.GET.get('q')
    if request.user.usertype == 0:
        if query:
            data = Jobs.objects.filter(title__icontains=query)
        else:
            data = Jobs.objects.all()
    else:
        if query:
            data = Jobs.objects.filter(userid=request.user.id, title__icontains=query)
        else:
            data = Jobs.objects.filter(userid=request.user.id)
    return render(request, 'view_jobs.html', {'data': data})


def editjobs(request,id):
    data=Jobs.objects.get(id=id)
    form = JobForm(request.POST,request.FILES,instance=data)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Job Edited Successfully', extra_tags='user_reg')
            return redirect('/viewjobs')
    else:
        form = JobForm(instance=data)
    return render(request,'register.html',{'form':form,'title':'Edit Job'})



def enrollcources(request,id):
        form=BookingForm(request.POST,request.FILES)
        if request.method == "POST":
                if form.is_valid():
                    lates=enroll.objects.latest('id')
                    lates.status=1
                    lates.save()
                    subject = 'Booking Enrollment Succesfull'
                    message = 'Your Enrollment for course '+str(lates.cource.title)+' Successfull'
                    from_email =  'EmpowerHerRise <hostemail>'
                    recipient_list = [lates.cource.userid.email]
                    send_mail(subject, message, from_email, recipient_list)
                    email = EmailMessage(subject, message,from_email=from_email,to=recipient_list)
                    email.send()
                    messages.success(request, f'Payement has been succesfull ! Enrolled Successfully ', extra_tags='user_reg')
                    return redirect('/viewcourses')  
        else:  
            book=enroll.objects.filter(userid=request.user.id,cource=id,status=1).first()
            if book:
                messages.success(request, f'Already Enrolled', extra_tags='user_reg')
                return redirect('/viewcourses')
            enroll.objects.create(
                userid=Register.objects.get(id=request.user.id),
                cource=courses.objects.get(id=id)
            )
            amt=courses.objects.get(id=id)
           
            return render(request,'register.html',{'form':form,'title':'Pay '+str(amt.Fees)+' Rs','payment':True})


def enrolledusers(request,id):
    if request.user.usertype == 2:
        data=enroll.objects.filter(cource=id,status=1)
    else:
       data=enroll.objects.filter(userid=id,status=1)
    return render(request,'view_enrolled.html',{'data':data})



def uploadcerti(request,id):
    form = uploadcertificateform(request.POST,request.FILES)
    certi= enroll.objects.get(id=id)
    username=certi.userid.username 
    if request.method=='POST':
        if form.is_valid():
           
            certi.certificate=form.cleaned_data['certificate']
            certi.save()
            messages.success(request, f'Certificate Uploaded Successfully '+str(username), extra_tags='user_reg')
            return redirect('/viewcourses')
    else:
        form = uploadcertificateform()
    return render(request,'register.html',{'form':form,'title':'Upload Certificate For '+str(username)})


def viewmorehostal(request,id):
    data=hostals.objects.get(id=id)
    feed=hostalfeedback.objects.filter(hostalid=id)
    return render(request,'view_more_hostals.html',{'data':data,'feed':feed})



def addhostalfeedback(request,id):
    if request.method=='POST':
            hostalfeedback.objects.create(
            hostalid=hostals.objects.get(id=id),
            userid=Register.objects.get(id=request.user.id),
            feedback=request.POST['comment'],
            ratings=request.POST['rating']
            )
            messages.success(request, f'Feedback Added Successfully', extra_tags='user_reg')
            return redirect('/viewhostals')
    else:
        return render(request,'add_feedback.html')



def viewmorecourse(request,id):
    if request.user.usertype == 0:
            book=enroll.objects.filter(userid=request.user.id,cource=id,status=1).first()
            if not book:
                messages.success(request, f'You Are Not Enrolled Course', extra_tags='user_reg')
                return redirect('/viewcourses')

    data=courses.objects.get(id=id)
    video=coursevideo.objects.filter(courseid=id)
    link=courseexams.objects.filter(courseid=id).order_by('current_time')
    return render(request,'view_more_course.html',{'data':data,'video':video,'link':link})


    
def addcourcevideo(request,id):
    form = coursevideoform(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.courseid=courses.objects.get(id=id)
            data.save()
            messages.success(request, f'Class Added Successfully', extra_tags='user_reg')
            return redirect('/viewcourses')
    else:
        form = coursevideoform()
    return render(request,'register.html',{'form':form,'title':'Add Class Video'})



def addlink(request,id):
    form = courselinkform(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            data=form.save(commit=False)
            data.courseid=courses.objects.get(id=id)
            data.current_time=timezone.now()
            data.save()
            messages.success(request, f'Link Added Successfully', extra_tags='user_reg')
            return redirect('/viewcourses')
    else:
        form = courselinkform()
    return render(request,'register.html',{'form':form,'title':'Add Class Link'})


def deletehostalfeedback(request,id):
    data=hostalfeedback.objects.get(id=id)
    data.delete()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or '/')



def deletecoursevideo(request,id):
    data=coursevideo.objects.get(id=id)
    data.delete()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or '/')


def deletecourselink(request,id):
    data=courseexams.objects.get(id=id)
    data.delete()
    referring_url = request.META.get('HTTP_REFERER')
    return redirect(referring_url or '/')


def viewmorejobs(request,id):
    data=Jobs.objects.get(id=id)
    return render(request,'view_more_jobs.html',{'data':data})