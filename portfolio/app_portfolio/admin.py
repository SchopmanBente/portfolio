from django.contrib import admin
from django.forms import ModelForm
from .models import  ProgrammingTechniques,ProgrammingLanguages,Image,PortfolioItem

# Register your models here.
admin.site.register(PortfolioItem)
admin.site.register(ProgrammingLanguages)
admin.site.register(ProgrammingTechniques)
admin.site.register(Image)

