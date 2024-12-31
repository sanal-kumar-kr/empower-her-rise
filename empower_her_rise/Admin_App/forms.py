from django import forms
from .models import *

class TalentgroupForm(forms.ModelForm):
    class Meta:
        model = Talentgroup
        fields = ['title','description']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "description" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
        }


class classesForm(forms.ModelForm):
    class Meta:
        model = classes
        fields = ['title','description','amount','start_time','end_time','date','class_type','place']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "description" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "amount" : forms.NumberInput(attrs={'class':'form-control','style':'','type':'number'}),
            "start_time" : forms.TextInput(attrs={'class':'form-control','style':'','type':'time'}),
            "end_time" : forms.TextInput(attrs={'class':'form-control','style':'','type':'time'}),
            "date" : forms.TextInput(attrs={'class':'form-control','style':'','type':'date'}),
            "class_type" : forms.Select(attrs={'class':'form-control','style':''}),
            "place" : forms.TextInput(attrs={'class':'form-control','style':''}),
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place'].required = False
        self.fields['amount'].required = False



class messageform(forms.ModelForm):
    
    class Meta:
        model = inbox
        fields = ['message']
        widgets = {
            "message" : forms.Textarea(attrs={'class':'form-control','style':'height :50px;'}),
        }
        help_texts = {
            'message' : None
        }


class videoform(forms.ModelForm):
    
    class Meta:
        model = classvideo
        fields = ['video']
        widgets = {
            "video" : forms.FileInput(attrs={'class':'form-control'}),
        }


class feedbackform(forms.ModelForm):
        
    class Meta:
        model = feedback
        fields = ['feedback']
        
        widgets = {
            "feedback" : forms.TextInput(attrs={'class':'style-input'}),
            }  

class replyform(forms.ModelForm):
        
    class Meta:
        model = feedback
        fields = ['reply']
        
        widgets = {
            "reply" : forms.TextInput(attrs={'class':'style-input'}),
            }  
      

class groupchatform(forms.ModelForm):

    class Meta:
        model = groupinbox
        fields = ['message']
        
        widgets = {
            "message" : forms.TextInput(attrs={'class':'style-input'}),
            }  
      

