from django import forms
from .models import *

#class MovieForm(forms.ModelForm):



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")