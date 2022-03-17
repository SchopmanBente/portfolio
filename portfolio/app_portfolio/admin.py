from django.contrib import admin
from .models import Navigation, NavigationUrlModel, ProgrammingTechniques,ProgrammingLanguages,Image,PortfolioItem

# Register your models here.
admin.site.register(PortfolioItem)
admin.site.register(ProgrammingLanguages)
admin.site.register(ProgrammingTechniques)
admin.site.register(Image)
admin.site.register(Navigation)
admin.site.register(NavigationUrlModel)