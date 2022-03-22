from modeltranslation.translator import  translator, TranslationOptions
from .models import NavigationPosition, NavigationApp,  NavigationAppPosition, ProgrammingTechniques,ProgrammingLanguages,Image,PortfolioItem

class  NavigationAppTranslationOptions(TranslationOptions):
    fields = ('app',)

class NavigationPositionTranslationOptions(TranslationOptions):
    fields = ('position',)

class NavigationAppPositionTranslationOptions(TranslationOptions):
    fields = ('app','position',)

class  ProgrammingTechniquesTranslationOptions(TranslationOptions):
    fields = ('technique',)

class ProgrammingLanguagesTranslationOptions(TranslationOptions):
    fields = ('language',)

class ImageTranslationOptions(TranslationOptions):
    fields = ('caption', 'image')

class PortfolioItemTranslationOptions(TranslationOptions):
    fields = ('image', 'title', 'description', 'gitHub_item_url')


translator.register(NavigationApp,NavigationAppTranslationOptions)
translator.register(NavigationPosition,NavigationPositionTranslationOptions)
translator.register(NavigationAppPosition, NavigationAppPositionTranslationOptions)
translator.register(ProgrammingTechniques,ProgrammingTechniquesTranslationOptions)
translator.register(ProgrammingLanguages,ProgrammingLanguagesTranslationOptions)
translator.register(Image,ImageTranslationOptions)
translator.register(PortfolioItem,PortfolioItemTranslationOptions)