from django.contrib import admin
from django.forms import ModelForm
from .models import  ProgrammingTechnique,ProgrammingLanguage,Image,PortfolioItem, Tag, OperatingSystem, Competence, Framework

# Register your models here.
admin.site.register(PortfolioItem)
admin.site.register(Tag)
admin.site.register(ProgrammingLanguage)
admin.site.register(ProgrammingTechnique)
admin.site.register(OperatingSystem)
admin.site.register(Competence)
admin.site.register(Image)
admin.site.register(Framework)

