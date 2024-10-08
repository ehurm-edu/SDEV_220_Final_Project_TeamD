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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("viewpets/", views.viewPet, name="viewpets"),
    path('pets/<int:petID>/', views.petDetail, name='petdetail'),
    path("viewfosters/", views.viewFoster, name="viewfoster"),
    path('fosters/<int:fosterID>/', views.fosterDetail, name="fosterdetail"),
    path("vieworgs/", views.viewOrg, name="vieworg"),
    path('orgs/<int:orgID>/', views.orgDetail, name="orgdetail"),
    path("addpet/", views.addPet, name="addpet"),
    path("addfoster/", views.addFoster, name="addfoster"),
    path("addorg/", views.addOrg, name="addorg"),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="index.html"), name='logout'),
    path("petsubmit", views.petsubmit, name="petsubmit"),
    path("fostersubmit", views.fostersubmit, name="fostersubmit"),
    path("orgsubmit", views.orgsubmit, name="orgsubmit"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)