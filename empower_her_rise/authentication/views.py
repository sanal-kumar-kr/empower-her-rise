from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . forms import *
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def index(request): 
    return render(request,'index.html')


def Home(request):
    return render(request,'layout.html')

def About(request):
    return render(request,'about.html')
    


def doLogin(request):
    form = LoginForm(request.POST,request.FILES)
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        print("username",username)
        print("password",password)
        user = authenticate(request,username=username,password=password)
        print(user)
        
        if user is None:
            return render(request,'index.html',{'form':form,'k':True})   
        elif user.status == 1:
            login(request, user)
            data = Register.objects.get(username=user)
            print(data)
            request.session['ut']=data.usertype
            data.usertype
            request.session['uid']=data.id
            data.usertype
            print(data.usertype)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'register.html',{'form':form,'title':'Login Here'})

def register(request):
    form = userregisterForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            
            try:
                email = form.cleaned_data["email"]
                Register.objects.get(email=email)
                
                return render(request,'login.html',{'form':form,'z':True})
            except Register.DoesNotExist:
                
                    Register.objects.create_user(
                        username = form.cleaned_data["username"],
                        email = form.cleaned_data["email"],
                        password = form.cleaned_data["password"],
                        contact = form.cleaned_data["contact"],
                        district = form.cleaned_data["district"],
                        pin = form.cleaned_data["pin"],
                        houseno = form.cleaned_data["houseno"],
                        street = form.cleaned_data["street"],
                        usertype=0
                       
                        )
                    messages.success(request, f'Your Registration has been succesfull ', extra_tags='user_reg')
                    return redirect('/')
    else:
        form = userregisterForm()
    return render(request,'register.html',{'form':form,'title':'Register As Public','validation':True})

def OrgRegister(request):
    form = orgregisterForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            try:
                email = form.cleaned_data["email"]
                Register.objects.get(email=email)
                return render(request,'login.html',{'form':form,'z':True})
            except Register.DoesNotExist:
                    Register.objects.create_user(
                        username = form.cleaned_data["username"],
                        email = form.cleaned_data["email"],
                        password = form.cleaned_data["password"],
                        contact = form.cleaned_data["contact"],
                        description = form.cleaned_data["description"],
                        id_proof = form.cleaned_data["id_proof"],
                        status=0,
                        usertype=2
                        )
                    messages.success(request, f'Your Registration has been succesfull  ', extra_tags='user_reg')
                    return redirect('/')
    else:
        form = orgregisterForm()
    return render(request,'register.html',{'form':form,'title':'Register As Organiztion','validation':True})

def DHOregister(request):
    form =  DHOregisterForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            try:
                email = form.cleaned_data["email"]
                Register.objects.get(email=email)
                return render(request,'login.html',{'form':form,'z':True})
            except Register.DoesNotExist:
                    Register.objects.create_user(
                        username = form.cleaned_data["username"],
                        email = form.cleaned_data["email"],
                        password = form.cleaned_data["password"],
                        qualification = form.cleaned_data["qualification"],
                        yearofexperience = form.cleaned_data["yearofexperience"],
                        contact = form.cleaned_data["contact"],
                        district = form.cleaned_data["district"],
                        id_proof = form.cleaned_data["id_proof"],
                        state = form.cleaned_data["state"],
                        usertype=3
                        )
                    messages.success(request, f'Your Registration has been succesfull', extra_tags='user_reg')
                    return redirect('/')
    else:
        form =  DHOregisterForm()
    return render(request,'register.html',{'form':form,'title':'Register As DHO','validation':True})

def policeofficerRegister(request):
    form = policeofficerregisterForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            
            try:
                email = form.cleaned_data["email"]
                Register.objects.get(email=email)
                return render(request,'login.html',{'form':form,'z':True})
            except Register.DoesNotExist:
                    Register.objects.create_user(
                        username = form.cleaned_data["username"],
                        password = form.cleaned_data["password"],
                        email = form.cleaned_data["email"],
                        rank = form.cleaned_data["rank"],
                        gender = form.cleaned_data["gender"],
                        contact = form.cleaned_data["contact"],
                        district = form.cleaned_data["district"],
                        id_proof = form.cleaned_data["id_proof"],
                        state = form.cleaned_data["state"],
                        usertype=4
                    )
                    messages.success(request, f'Your Registration has been succesfull ', extra_tags='user_reg')
                    return redirect('/')
    else:
        form = policeofficerregisterForm()
    return render(request,'register.html',{'form':form,'title':'Register As PoliceOfficer','validation':True})




def bookclass(request,id):
        form=BookingForm(request.POST,request.FILES)
        if request.method == "POST":
             if form.is_valid():
                lates=booking.objects.latest('id')
                lates.status=1
                lates.save()
                subject = 'Booking Successfull'
                message = 'Your Booking for '+str(lates.classid.title)+' Successfull'
                from_email =  'EmpowerHerRise <hostemail>'
                recipient_list = [lates.classid.userid.email]
                send_mail(subject, message, from_email, recipient_list)
                email = EmailMessage(subject, message,from_email=from_email,to=recipient_list)
                email.send()
                messages.success(request, f'Payement has been succesfull  ', extra_tags='user_reg')

                return redirect('/viewclasses')  
        else:  
            book=booking.objects.filter(user=request.user.id,classid=id,status=1).first()
            if book:
                messages.success(request, f'Already Booked', extra_tags='user_reg')
                return redirect('/viewclasses')
            booking.objects.create(
            user=Register.objects.get(id=request.user.id),
          classid=classes.objects.get(id=id)
            )
            amt=classes.objects.get(id=id)
           
            return render(request,'register.html',{'form':form,'title':'Pay '+str(amt.amount)+' Rs','payment':True})

def dologout(request):
     auth.logout(request)
     return redirect('/')