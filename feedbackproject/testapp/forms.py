from django import forms
from django.core import validators
from captcha.fields import CaptchaField

# class FeedBackForm(forms.Form):
#     name=forms.CharField()
#     rollno=forms.IntegerField()
#     email=forms.EmailField()
#     name=forms.CharField()
#     feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator])
#     def clean_name(self):
#         print('Validating name field')
#         inputname=self.cleaned_data['name']
#         if len(inputname)<4:
#             raise forms.ValidationError('The minimum number of characters in name field should be 4')
#         return inputname
#     def clean_rollno(self):
#           print('Validating roll no field')
#           inputrollno=self.cleaned_data['rollno']
#           return inputrollno
#     def clean_email(self):
#          print('Validating email field')
#          inputemail=self.cleaned_data['email']
#          return inputemail
#     def clean_feedback(self):
#          print("Validating feedback form")
#          inputfeedback=self.cleaned_data['feedback']
#          return inputfeedback



# def starts_with_d(value):
#     print('d function execution')
#     if value[0].lower()!='d':
#         raise forms.ValidationError('Name Should starts with d or D!')
    
# def gmail_check(value):
#     if value[-10:]!='@gmail.com':
#         raise forms.ValidationError('Mail extension should be gmail!!')

# class FeedBackForm(forms.Form):
#     name=forms.CharField(validators=[starts_with_d])
#     rollno=forms.IntegerField()
#     email=forms.EmailField()
#     feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])




class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='password(Again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
    captcha=CaptchaField()

    def clean(self):
        print('Total form Validation.....')
        total_cleaned_data=super().clean()
        print('Validating Name')
        inputname=total_cleaned_data['name']
        if inputname[0].lower()!='d':
            raise forms.ValidationError('Name should starts with d')
        inputmail=total_cleaned_data['email']
        if inputmail[-10:]!='@gmail.com':
            raise forms.ValidationError('email extension should be gmail')
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['rpassword']
        if pwd!=rpwd:
            raise forms.ValidationError('Both password must be same.')
        bot_handler_value=total_cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Hello BOT How are you.')

