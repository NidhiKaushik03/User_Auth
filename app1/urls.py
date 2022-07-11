from django.contrib import admin
from django.urls import path
#from .views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home_Page'),
     
]