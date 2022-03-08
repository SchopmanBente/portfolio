from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
class LandingPage_Admin( admin.ModelAdmin ):
    form = LandingPageForm