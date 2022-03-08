from django import forms
from django.db import models


class LandingPageForm(forms.ModelForm ):
    gitHub_url = models.CharField()
    linkedin_url = models.CharField()
    gitHub_logo = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    linkedin_logo = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    title = models.CharField()
    descr = forms.CharField(widget=forms.Textarea)
    email = models.EmailField()