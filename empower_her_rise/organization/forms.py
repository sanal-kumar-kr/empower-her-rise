from django import forms
from .models import *

class CorceForm(forms.ModelForm):
    class Meta:
        model = courses
        fields = ['title','courceimage','description','Fees','Duration']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "description" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "Fees" : forms.NumberInput(attrs={'class':'form-control','style':''}),
            "Duration" : forms.TextInput(attrs={'class':'form-control','style':''}),

        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['firm_name','location','firmimage','title','description','qualification','address','email']
        widgets = {
            "firm_name" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "location" : forms.TextInput(attrs={'class':'form-control','style':''}),

            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "description" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "qualification" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "address" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "email" : forms.TextInput(attrs={'class':'form-control','style':''}),

        }



class hostalForm(forms.ModelForm):
    class Meta:
        model = hostals
        fields = ['hostal_name','hostalimage','location','address','Rent','Tenant_preferred','contact','rule','facilities']
        widgets = {
            "hostal_name" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "location" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "address" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "Rent" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "Tenant_preferred" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "contact" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "rule" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "facilities" : forms.TextInput(attrs={'class':'form-control','style':''}),

        }


class uploadcertificateform(forms.ModelForm):
    class Meta:
        model = enroll
        fields = ['certificate']
        widgets = {
            "certificate" : forms.FileInput(attrs={'class':'form-control','style':''}),
           
        }



class coursevideoform(forms.ModelForm):
    class Meta:
        model = coursevideo
        fields = ['classvideo']
        widgets = {
            "classvideo" : forms.FileInput(attrs={'class':'form-control','style':''}),
           
        }


class courselinkform(forms.ModelForm):
    class Meta:
        model = courseexams
        fields = ['link']
        widgets = {
            "link" : forms.TextInput(attrs={'class':'form-control','style':''}),
           
        }