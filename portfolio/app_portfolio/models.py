from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class NavigationApp(models.Model):
    app = models.CharField(max_length=250)

    def __str__(self):
        return self.app


class NavigationPosition(models.Model):
    position = models.IntegerField()

    def __str__(self):
        return str(self.position)


class NavigationAppPosition(models.Model):
    app = models.ForeignKey(NavigationApp, on_delete=models.CASCADE)
    position = models.ForeignKey(NavigationPosition, on_delete=models.CASCADE)

    def __str__(self):
        return "app: {} position: {}".format(self.app, str(self.position))


class ProgrammingTechniques(models.Model):
    technique = models.CharField(max_length=150)

    def __str__(self):
        return self.technique


class ProgrammingLanguages(models.Model):
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
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2500, help_text=_(portfolio_item_instruction_text))
    programminglanguages = models.ManyToManyField(ProgrammingLanguages)
    programmingtechniques = models.ManyToManyField(ProgrammingTechniques)
    gitHub_item_url = models.CharField(max_length=500, help_text=_("Github url from the project"))

    def __str__(self):
        return self.title
