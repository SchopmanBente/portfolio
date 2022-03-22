from modeltranslation.translator import  translator, TranslationOptions
from .models import LandingPage, Image, Document , NavigationApp, NavigationPosition, NavigationAppPosition


class  NavigationAppTranslationOptions(TranslationOptions):
    fields = ('app',)

class NavigationPositionTranslationOptions(TranslationOptions):
    fields = ('position',)

class NavigationAppPositionTranslationOptions(TranslationOptions):
    fields = ('app','position',)


class LandingPageTranslationOptions(TranslationOptions):
    fields = ('picture', 'title', 'subtitle', 'about', 'gitHub_url', 'linkedin_url', 'cv', 'email')

class ImageTranslationOptions(TranslationOptions):
    fields = ('caption', 'image')

class DocumentTranslationOptions(TranslationOptions):
    fields = ('caption', 'document')

translator.register(NavigationApp,NavigationAppTranslationOptions)
translator.register(NavigationPosition,NavigationPositionTranslationOptions)
translator.register(NavigationAppPosition, NavigationAppPositionTranslationOptions)
translator.register(LandingPage, LandingPageTranslationOptions)
translator.register(Image,ImageTranslationOptions)
translator.register(Document,DocumentTranslationOptions)