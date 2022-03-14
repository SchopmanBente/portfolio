import os

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadhandler import FileUploadHandler
from django.utils.translation import gettext_lazy as _

# Create your models here.



ifs = FileSystemStorage(location='/media/photos')
dfs = FileSystemStorage(location='/media/documents')



class SingletonModel(models.Model):
    _singleton = models.BooleanField(default=True, editable=False, unique=True)

    class Meta:
        abstract = True


class LandingPage(SingletonModel):

    picture = models.ImageField(upload_to='pictures', storage=ifs, help_text=_("Choose a picture for the landingpage"))
    title = models.CharField(max_length=500, help_text=_("Title"))
    subtitle = models.CharField(max_length=500, help_text=_("Subtitle"))
    about = models.TextField(max_length=2500 ,help_text=_("About"))
    gitHub_url = models.CharField(max_length=500, help_text=_("Github_url"))
    linkedin_url = models.CharField(max_length=500, help_text=_("LinkedIn url"))
    cv = models.FileField(db_index=True, upload_to='documents', storage=dfs, help_text=_("Upload your CV!"))
    email = models.EmailField(help_text=_("How can people reach you?"))



