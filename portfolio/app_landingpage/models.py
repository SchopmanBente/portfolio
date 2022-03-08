from django import forms
from django.db import models


# Create your models here.
class MultilingualModel(models.Model):
    # fallback/default language code
    default_language = None

    # currently selected language
    selected_language = None

    class Meta:
        abstract = True

    def select_language(self, lang):
        """Select a language"""
        self.selected_language = lang
        return self

    def __getattribute__(self, name):
        def get(x):
            return super(MultilingualModel, self).__getattribute__(x)

        try:
            # Try to get the original field, if exists
            value = get(name)
            # If we can select language on the field as well, do it
            if isinstance(value, MultilingualModel):
                value.select_language(get('selected_language'))
                return value
        except AttributeError as e:
            # Try the translated variant, falling back to default if no
            # language has been explicitly selected
            lang = self.selected_language
            if not lang:
                lang = self.default_language
            if not lang:
                raise
            value = get(name + '_' + lang)
            # If the translated variant is empty, fallback to default
            if isinstance(value, basestring) and value == u'':
                value = get(name + '_' + self.default_language)

        return value

class LandingPage(MultilingualModel):
    picture = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    about = models.TextField(max_length=2500)
    gitHub_url = models.CharField(max_length=500)
    gitHub_logo = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    linkedin_url = models.CharField(max_length=500)
    linkedin_logo = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    cv = models.FileField(db_index=True, upload_to='CV')
    email = models.EmailField()