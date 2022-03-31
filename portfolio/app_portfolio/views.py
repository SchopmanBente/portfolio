from django.contrib.sites import requests
from django.shortcuts import render
from .models import ProgrammingLanguage
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
    programminglanguages = ProgrammingLanguage.objects.all()
    programminglanguages_as_json = serializers.serialize("json", ProgrammingLanguage.objects.all())
    return render(request, 'portfolio-1.html', {'programminglanguages': programminglanguages_as_json})
