"""
URL configuration for SDev220Final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from PetTracker import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("addfoster.html", views.addFoster, name="addfoster"),
    path("addorg.html", views.addOrg, name="addorg"),
    path("addpet.html", views.addPet, name="addpet"),
    path("fostersubmit.html", views.fosterSubmit, name="fostersubmit"),
    path("index.html", views.index, name="index"),
    path("orgsubmit.html", views.orgSubmit, name="orgsubmit"),
    path("petsubmit.html", views.petSubmit, name="petsubmit"),
    path("viewpets.html", views.viewPet, name="viewpets"),
    path("", views.index, name="rootview"),
    
    
    
    

]
