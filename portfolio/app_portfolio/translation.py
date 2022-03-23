from modeltranslation.translator import  translator, TranslationOptions
from .models import ProgrammingTechniques,ProgrammingLanguages,Image,PortfolioItem



class  ProgrammingTechniquesTranslationOptions(TranslationOptions):
    fields = ('technique',)

class ProgrammingLanguagesTranslationOptions(TranslationOptions):
    fields = ('language',)

class ImageTranslationOptions(TranslationOptions):
    fields = ('caption', 'image')

class PortfolioItemTranslationOptions(TranslationOptions):
    fields = ('image', 'title', 'description', 'gitHub_item_url')

translator.register(ProgrammingTechniques,ProgrammingTechniquesTranslationOptions)
translator.register(ProgrammingLanguages,ProgrammingLanguagesTranslationOptions)
translator.register(Image,ImageTranslationOptions)
translator.register(PortfolioItem,PortfolioItemTranslationOptions)