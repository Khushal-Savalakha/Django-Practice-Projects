from django import forms
from testapp.models import Movie

class MovieForm(forms.ModelForm):
    def rating_validator(value):
        if value<5:
            raise forms.ValidationError()
    rating=forms.IntegerField(validators=[rating_validator])
    class Meta:
        model=Movie
        fields='__all__'