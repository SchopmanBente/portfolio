from modeltranslation.translator import  translator, TranslationOptions
from .models import ProgrammingTechnique,ProgrammingLanguage,Image,PortfolioItem, Tag, OperatingSystem, Competence, Framework

class TagTranslationOptions(TranslationOptions):
    fields = ('tag',)

class  ProgrammingTechniqueTranslationOptions(TranslationOptions):
    fields = ('technique',)

class ProgrammingLanguageTranslationOptions(TranslationOptions):
    fields = ('language',)

class ImageTranslationOptions(TranslationOptions):
    fields = ('caption', 'image')

class PortfolioItemTranslationOptions(TranslationOptions):
    fields = ('image', 'title', 'description', 'gitHub_item_url',)

class OperatingSystemTranslationOptions(TranslationOptions):
    fields = ('os', )

class CompetenceTranslationOptions(TranslationOptions):
    fields = ('skill',)

class  FrameworkTranslationOptions(TranslationOptions):
    fields = ('framework',)
translator.register(ProgrammingTechnique,ProgrammingTechniqueTranslationOptions)
translator.register(ProgrammingLanguage,ProgrammingLanguageTranslationOptions)
translator.register(Image,ImageTranslationOptions)
translator.register(PortfolioItem,PortfolioItemTranslationOptions)
translator.register(Tag,TagTranslationOptions)
translator.register(OperatingSystem, OperatingSystemTranslationOptions)
translator.register(Competence,CompetenceTranslationOptions)
translator.register(Framework, FrameworkTranslationOptions)