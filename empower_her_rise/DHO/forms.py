from django import forms
from .models import *

class healthcheckupForm(forms.ModelForm):
    class Meta:
        model = healthcheckup
        fields = ['title','description','time','date','place']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "place" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "description" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "time" : forms.TimeInput(attrs={'class':'form-control','type':'time',}),
            "date" : forms.DateInput(attrs={'class':'form-control','type':'date'}),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].required = False


class SchemasForm(forms.ModelForm):
    class Meta:
        model = Schemas
        fields = ['title','description','required','link']
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control','style':''}),
            "required" : forms.Textarea(attrs={'class':'form-control','style':''}),
            "description" : forms.Textarea(attrs={'class':'form-control','style':'height:100px'}),
            "link" : forms.TextInput(attrs={'class':'form-control','style':''}),


        }









