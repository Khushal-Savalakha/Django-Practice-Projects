from django import forms

class StudentForm(forms.Form):
    name=forms.CharField() #here max_length is optional
    marks=forms.IntegerField()
    age=forms.IntegerField()