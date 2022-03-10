import os

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadhandler import FileUploadHandler
# Create your models here.


ifs = FileSystemStorage(location='/media/photos')
dfs = FileSystemStorage(location='/media/documents')

class SingletonModel(models.Model):
    _singleton = models.BooleanField(default=True, editable=False, unique=True)

    class Meta:
        abstract = True


class LandingPage(SingletonModel):

    #picture = models.ImageField(upload_to='pictures', storage=ifs)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    about = models.TextField(max_length=2500)
    gitHub_url = models.CharField(max_length=500)
    linkedin_url = models.CharField(max_length=500)
    #cv = models.FileField(db_index=True, upload_to='documents', storage=dfs)
    email = models.EmailField()



