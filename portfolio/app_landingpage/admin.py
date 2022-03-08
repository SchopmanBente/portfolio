from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib import admin
from app_landingpage.models import LandingPage

admin.site.register(LandingPage)
