from django.http import HttpRequest, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import LandingPage

# Create your views here.
""" 
def get_object(self):
    pk = self.kwargs.get('pk')
    try:
        return LandingPage.objects.get(pk=pk)
    except LandingPage.DoesNotExist:
        raise Http404


 def get(self,request, *args, **kwargs):
        # ...
        pass
        
 def index(request, *args, **kwargs):
    pk = self.kwargs.get('pk')
    try:
        return LandingPage.objects.get(pk=pk)
    except LandingPage.DoesNotExist:
        raise Http404
    landingpage_pk = kwargs.get('pk')
    landingpage = get_object_or_404(LandingPage, landingpage_pk)
    return render(request, "app_landingpage/index.html", {'landingpage': landingpage, })

"""
def index(request):
    try:
        lp = LandingPage.objects.get(pk=1)
        return render(request, "index.html", {"landingpage": lp})
    except LandingPage.DoesNotExist:
        raise Http404("No Landingpage matches the given query.")

