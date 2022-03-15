from django.template.context_processors import static
from django.template.defaulttags import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'app_landingspage'

urlpatterns = [
    path('', views.index, name="index"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

