from django.http import HttpRequest, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import LandingPage, Image

# Create your views here.
def image_index(request):
    pics=Image.objects.all()
    return render(request, "index.html", {"pics":pics})
def index(request):
    try:
        lp = LandingPage.objects.get(pk=1)
        return render(request, "index.html", {"landingpage": lp})
    except LandingPage.DoesNotExist:
        raise Http404("No Landingpage matches the given query.")

