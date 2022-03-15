"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_landingpage.urls', namespace='landingpage')),
    path('skills/', include('app_skills.urls', namespace='skills')),
    path('work/', include('app_workexperience.urls', namespace='work')),
    path('portfolio/', include('app_portfolio.urls', namespace='portfolio')),
    path('i18n/', include('django.conf.urls.i18n')),
]


i18n_patterns  = [
    path(_('nl/'), include('app_nl.urls')),
    path('', include('app_landingpage.urls')),
]
urlpatterns += i18n_patterns

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)