from django.contrib import admin
from django.forms import ModelForm
from .models import NavigationPosition, NavigationApp,  NavigationAppPosition, ProgrammingTechniques,ProgrammingLanguages,Image,PortfolioItem

# Register your models here.
admin.site.register(PortfolioItem)
admin.site.register(ProgrammingLanguages)
admin.site.register(ProgrammingTechniques)
admin.site.register(Image)
admin.site.register(NavigationAppPosition)
admin.site.register(NavigationApp)
admin.site.register(NavigationPosition)

class NavigationPositionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["position"].required = True

    class Meta:
        model = NavigationPosition
        fields = '__all__'
        proxy = True

class NavigationAppForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["app"].required = True

    class Meta:
        model = NavigationApp
        fields = '__all__'
        proxy = True
