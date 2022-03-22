import os
from app_landingpage.models import LandingPage , Image, Document, NavigationAppPosition, NavigationApp, NavigationPosition
from django.contrib import admin
# Register your models here
from django.forms import ModelForm
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadhandler import FileUploadHandler
from django.shortcuts import render


admin.site.register(LandingPage)
admin.site.register(Document)
admin.site.register(Image)
admin.site.register(NavigationAppPosition)
admin.site.register(NavigationApp)
admin.site.register(NavigationPosition)


class ImageAdmin(admin.ModelAdmin):
    class Meta:
        model = Image
    fields = ('image_tag',)
    readonly_fields = ('image_tag',)

class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["picture"].required = True
        self.fields["title"].required = True
        self.fields["subtitle"].required = True
        self.fields["about"].required = True
        self.fields["gitHub_url"].required = True
        self.fields["linkedin_url"].required = True
        self.fields["cv"].required = True
        self.fields["email"].required = True

    class Meta:
        model = LandingPage
        fields = '__all__'
        proxy = True
    """ 
    def post(self,request):
        #self.simple_upload(request)
        lp = LandingPage(title=request["title"], subtitle=request["subtitle"], about=request["about"], gitHub_url=request["gitHub_url"], linkedin_url=request["linkedin_url"],
                         email = request["email"])
        lp.save()
    """


    def simple_upload(self,request):
        if request.method == 'POST' and request.FILES['cv']:
            cv = request.FILES['cv']
            fs = FileSystemStorage()
            filename = fs.save(cv.name, cv)
            uploaded_file_url = fs.url(filename)
            return render(request, 'core/simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })

    """
    def post(self, request):
        mediaRoot = os.path.join(settings.MEDIA_ROOT, 'media/')
        picture = mediaRoot + request["landingpage.picture"]
        cv = mediaRoot + request["landingpage.cv"]
        input = {
            "picture": picture,
            "title": request["landingpage.title"],
            "subtitle": request["landingpage.subtitle"],
            "about": request["landingpage.about"],
            "gitHub_url": request["landingpage.gitHub_url"],
            "linkedin_url": request["landingpage.linkedin_url"],
            "cv": cv,
            "email": request["email"],
        }
        lp = LandingPage(picture=input["picture"], title=input["title"], subtitle=input["subtitle"],
                         about=input["about"], gitHub_url=input["gitHub_url"],
                         linkedin_url=input["linkedin_url"], cv=input["cv"], email=input["email"])
        lp.save()
        """
