from django import forms
from app.models import *

class SchoolForms(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'

class StudentForms(forms.ModelForm):
    class Meta:
        model=Student
        exclude=['sid']