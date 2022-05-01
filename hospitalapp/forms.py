from django import forms 
from .models import patient,doctor

class patientform(forms.ModelForm):
    class Meta:
        model=patient
        fields=['name','phno','email','Disease','Description','password']
        widgets={
                'name':forms.TextInput(attrs={'style':'margin:5px'}),
                'phno':forms.TextInput(attrs={'style':'margin:5px'}),
                'Disease':forms.TextInput(attrs={'style':'margin:5px'}),
                'Description':forms.Textarea(attrs={'style':'margin:5px'}),
                'password':forms.TextInput(attrs={'style':'margin:5px'}),
                }

class doctorform(forms.ModelForm):
    class Meta:
        model=doctor
        fields="__all__"

        