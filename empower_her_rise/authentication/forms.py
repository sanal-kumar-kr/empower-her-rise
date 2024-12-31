from django import forms
from . models import *
from Admin_App.models import *


class userregisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username','email','password','contact','district','pin','street','houseno']
        
        widgets = {
            "username" : forms.TextInput(attrs={'class':'style-input'}),
            "email" : forms.EmailInput(attrs={'class':'style-input'}),
            "contact" : forms.TextInput(attrs={'class':'style-input','maxlength':'10'}),
            "password" : forms.PasswordInput(attrs={'class':'style-input','maxlength':'10'}),
            "district" : forms.Select(attrs={'class':'style-input'}),
            "pin" : forms.TextInput(attrs={'class':'style-input'}),
            "street" : forms.TextInput(attrs={'class':'style-input'}),
            "houseno" : forms.TextInput(attrs={'class':'style-input'}),
            }
        help_texts = {
            'username' : None,
            'email' : '',
            'contact' : '',
            'password' : '',
        } 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['contact'].required = False
        self.fields['password'].required = False                               
                      
        
class LoginForm(forms.ModelForm):
        
    class Meta:
        model = Register
        fields = ['username','password']
        
        widgets = {
            "username" : forms.TextInput(attrs={'class':'style-input'}),
            "password" : forms.PasswordInput(attrs={'class':'style-input','maxlength':'10'}),
            }  
        help_texts = {
            'username' : None,
           
            'password':''
        }
        
class orgregisterForm(forms.ModelForm):
        
    class Meta:
        model = Register
        fields = ['username','email','password','contact','description','id_proof']
        widgets = {
            "username" : forms.TextInput(attrs={'class':'style-input'}),
            "email" : forms.EmailInput(attrs={'class':'style-input'}),
            "contact" : forms.TextInput(attrs={'class':'style-input','maxlength':'10'}),
            "password" : forms.PasswordInput(attrs={'class':'style-input','maxlength':'10'}),
            "description" : forms.TextInput(attrs={'class':'style-input'}),
            "id_proof" : forms.FileInput(attrs={'class':'style-input'}),
             }
        help_texts = {
            'username' : None,
            'email' : '',
            'contact' : '',
            'password' : '',
        } 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['contact'].required = False
        self.fields['password'].required = False                               
        
class DHOregisterForm(forms.ModelForm):
        
    class Meta:
        model = Register
        fields = ['username','gender','email','contact','password','qualification','yearofexperience','id_proof','district','state']
        
        widgets = {
            "username" : forms.TextInput(attrs={'class':'style-input'}),
            "gender" : forms.Select(attrs={'class':'style-input'}),
            "email" : forms.EmailInput(attrs={'class':'style-input'}),
            "contact" : forms.TextInput(attrs={'class':'style-input','maxlength':'10'}),
            "password" : forms.PasswordInput(attrs={'class':'style-input','maxlength':'10'}),

            "qualification" : forms.TextInput(attrs={'class':'style-input'}),
            "yearofexperience" : forms.TextInput(attrs={'class':'style-input'}),
            "id_proof" : forms.FileInput(attrs={'class':'style-input'}),
            "district" : forms.Select(attrs={'class':'style-input'}),
            "state" : forms.Select(attrs={'class':'style-input'}),
            }   
        help_texts = {
            'username' : None,
            'email' : '',
            'contact' : '',
            'password' : '',
        } 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['contact'].required = False
        self.fields['password'].required = False                            
class policeofficerregisterForm(forms.ModelForm):
        
    class Meta:
        model = Register
        fields = ['username','contact','email','password','gender','rank','id_proof','district','state']
        
        widgets = {
            "username" : forms.TextInput(attrs={'class':'style-input'}),
            "contact" : forms.TextInput(attrs={'class':'style-input'}),
            "email" : forms.EmailInput(attrs={'class':'style-input'}),

            "password" : forms.PasswordInput(attrs={'class':'style-input','maxlength':'10'}),
            "gender" : forms.Select(attrs={'class':'style-input'}),
            "rank" : forms.TextInput(attrs={'class':'style-input'}),
            "district" : forms.Select(attrs={'class':'style-input'}),
            "state" : forms.Select(attrs={'class':'style-input'}),
            "id_proof" : forms.FileInput(attrs={'class':'style-input'}),
            }     
        help_texts = {
            'username' : None,
            'email' : '',
            'contact' : '',
            'password' : '',
        } 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False
        self.fields['contact'].required = False
        self.fields['password'].required = False       



class BookingForm(forms.Form):
    CardNumber = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'style-input'})
    )
    CVV = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'style-input'})
    )
    ExpiryDate = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'style-input'})
    )




 




