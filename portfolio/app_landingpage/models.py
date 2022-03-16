from django.db import models
from django.db.models import ForeignKey
from django.utils.translation import gettext_lazy as _

import os


# Create your models here

def get_upload_path_image(instance, filename):
    return os.path.join("media/pictures/%s" % instance.image.image.url, filename)

class Image(models.Model):
    caption =  models.CharField(max_length=50)
    image = models.ImageField(upload_to='images',help_text=_("Choose a picture for the landingpage"))

    def __str__(self):
        return self.caption




class Document(models.Model):
    caption = models.CharField(max_length=50)
    document = models.FileField(db_index=True, upload_to='documents', help_text=_("Upload your CV!"))

    def __str__(self):
        return self.caption


class SingletonModel(models.Model):
    _singleton = models.BooleanField(default=True, editable=False, unique=True)

    class Meta:
        abstract = True


class LandingPage(SingletonModel):
    picture = ForeignKey(Image, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, help_text=_("Title"))
    subtitle = models.CharField(max_length=500, help_text=_("Subtitle"))
    about = models.TextField(max_length=2500, help_text=_("About"))
    gitHub_url = models.CharField(max_length=500, help_text=_("Github_url"))
    linkedin_url = models.CharField(max_length=500, help_text=_("LinkedIn url"))
    cv = ForeignKey(Document, on_delete=models.CASCADE)
    email = models.EmailField(help_text=_("How can people reach you?"))
