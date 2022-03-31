from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class OperatingSystem(models.Model):
    os = models.CharField(max_length=75)

    def __str__(self):
        return self.os

class Framework(models.Model):
    framework = models.CharField(max_length=100)

    def __str__(self):
        return  self.framework

class Competence(models.Model):
    skill = models.CharField(max_length=75)

    def __str__(self):
        return self.skill


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class ProgrammingTechnique(models.Model):
    technique = models.CharField(max_length=150)

    def __str__(self):
        return self.technique


class ProgrammingLanguage(models.Model):
    language = models.CharField(max_length=150)

    def __str__(self):
        return self.language


class Image(models.Model):
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', help_text=_("Choose a picture for the landingpage"))

    def __str__(self):
        return self.caption


class PortfolioItem(models.Model):
    portfolio_item_instruction_text = 'Try answering some of these questions. 1)Why did you choose to build this project? 2)What challenged you when making this project?3)What did you learn from making this project?4)What learnings have you taken with you into other projects? 5)What would you do differently next time?'
    portfolio_item_instruction_text.join(
        "6)Did you get stuck at any point? How did you get unstuck? 7)What was your process for completing this project? 8) Did you do wireframes, make a Trello board, or did you just get stuck into it?")
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='main image of the project+')
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2500, help_text=_(portfolio_item_instruction_text))
    oses = models.ManyToManyField(OperatingSystem)
    competence = models.ManyToManyField(Competence)
    programminglanguages = models.ManyToManyField(ProgrammingLanguage)
    programmingtechniques = models.ManyToManyField(ProgrammingTechnique)
    frameworks = models.ManyToManyField(Framework)
    gitHub_item_url = models.CharField(max_length=500, help_text=_("Github url from the project"))
    tag = models.ManyToManyField(Tag)
    images = models.ManyToManyField(Image, related_name='project_images+')

    def __str__(self):
        return self.title
