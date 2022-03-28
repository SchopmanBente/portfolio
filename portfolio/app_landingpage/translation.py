from modeltranslation.translator import  translator, TranslationOptions
from .models import LandingPage, Image, Document

class LandingPageTranslationOptions(TranslationOptions):
    fields = ('picture', 'title', 'subtitle', 'about', 'gitHub_url', 'linkedin_url', 'cv', 'email')

class ImageTranslationOptions(TranslationOptions):
    fields = ('caption', 'image')

class DocumentTranslationOptions(TranslationOptions):
    fields = ('caption', 'document')

translator.register(LandingPage, LandingPageTranslationOptions)
translator.register(Image,ImageTranslationOptions)
translator.register(Document,DocumentTranslationOptions)