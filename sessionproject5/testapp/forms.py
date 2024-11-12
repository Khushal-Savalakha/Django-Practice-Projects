from django import forms

class NameForm(forms.Form):
    name=forms.CharField(max_length=100)

class AgeForm(forms.Form):
    age=forms.IntegerField()

class FriendForm(forms.Form):
    friend=forms.CharField(max_length=100)
    # age=forms.IntegerField()