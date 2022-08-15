from django import forms
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):
    name=forms.CharField(max_length=10,required=False)
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {'password':forms.PasswordInput}