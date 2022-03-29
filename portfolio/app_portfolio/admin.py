from django.contrib import admin
from django.forms import ModelForm
from .models import  ProgrammingTechnique,ProgrammingLanguage,Image,PortfolioItem, Tag

# Register your models here.
admin.site.register(PortfolioItem)
admin.site.register(Tag)
admin.site.register(ProgrammingLanguage)
admin.site.register(ProgrammingTechnique)
admin.site.register(Image)

