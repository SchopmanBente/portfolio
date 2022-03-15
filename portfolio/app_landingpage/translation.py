from modeltranslation.translator import  translator, TranslationOptions
from .models import LandingPage


class LandingPageTranslationOptions(TranslationOptions):
    fields = ('picture', 'title', 'subtitle', 'about', 'gitHub_url', 'linkedin_url', 'cv', 'email')

translator.register(LandingPage, LandingPageTranslationOptions)
