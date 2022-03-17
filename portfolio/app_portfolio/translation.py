from modeltranslation.translator import  translator, TranslationOptions
from .models import Navigation, NavigationUrlModel, ProgrammingTechniques,ProgrammingLanguages,Image,PortfolioItem

class NavigationUrlModelTranslationOptions(TranslationOptions):
    fields = ('model',)

class NavigationTranslationOptions(TranslationOptions):
    fields = ('position','urlModel')

class  ProgrammingTechniquesTranslationOptions(TranslationOptions):
    fields = ('technique',)

class ProgrammingLanguagesTranslationOptions(TranslationOptions):
    fields = ('language',)

class ImageTranslationOptions(TranslationOptions):
    fields = ('caption', 'image')

class PortfolioItemTranslationOptions(TranslationOptions):
    fields = ('image', 'title', 'description', 'gitHub_item_url')


translator.register(Navigation,NavigationTranslationOptions)
translator.register(NavigationUrlModel,NavigationUrlModelTranslationOptions)
translator.register(ProgrammingTechniques,ProgrammingTechniquesTranslationOptions)
translator.register(ProgrammingLanguages,ProgrammingLanguagesTranslationOptions)
translator.register(Image,ImageTranslationOptions)
translator.register(PortfolioItem,PortfolioItemTranslationOptions)