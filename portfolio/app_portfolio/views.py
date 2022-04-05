from django.contrib.sites import requests
from django.shortcuts import render
from .models import ProgrammingLanguage, ProgrammingTechnique, OperatingSystem, Competence,  Framework
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
    programminglanguages_as_json = serializers.serialize("json", ProgrammingLanguage.objects.all())
    programmingtechniques_as_json = serializers.serialize("json", ProgrammingTechnique.objects.all())
    os_as_json = serializers.serialize("json", OperatingSystem.objects.all())
    competence_as_json = serializers.serialize("json", Competence.objects.all())
    framework_as_json = serializers.serialize("json", Framework.objects.all())
    return render(request, 'portfolio-1.html', {'programminglanguages': programminglanguages_as_json,'programmingtechniques': programmingtechniques_as_json,
                                                'oses': os_as_json, 'competence': competence_as_json, 'framework': framework_as_json})
