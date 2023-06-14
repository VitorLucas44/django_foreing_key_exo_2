"""
URL configuration for testdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from cars.views import liste_voitures, voitures_par_couleur

from django.urls import path
from cars.views import liste_voitures, voitures_par_couleur

urlpatterns = [
    path('', liste_voitures, name='home'),
    path('voitures/', liste_voitures, name='liste_voitures'),
    path('voitures-par-couleur/', voitures_par_couleur, name='voitures_par_couleur'),
]
