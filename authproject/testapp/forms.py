from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        #here there is too many fields in User
        #  because it is default database like permissions related and etc
        # fields='__all__'
        fields=['username','password','email','first_name','last_name']