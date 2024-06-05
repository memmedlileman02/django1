"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path ,include
from films.views import *

urlpatterns = [
    path("",home__view, name="home"),
    path("about",about__view, name="about"),
    path("contact",contact__view, name="contact"),
    path("filmm",filmm__view, name="filmm"),
    path("addfilms",addfilms__view, name="addfilms"),
    path("update/<int:id>",films__update__view, name="update"),
    path("delete/<int:id>",films__delete__view, name="delete"),
    path("films-detail/<int:id>",films__detail__view, name="films-detail"),
    path("dashboard",dashboard__view, name="dashboard"),
    path("account/",include("account.urls")),
    path('admin/', admin.site.urls),
    path("comment/<int:id>",addcomment__view, name="comment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)