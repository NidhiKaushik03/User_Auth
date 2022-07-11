from django.contrib import admin
from django.urls import path
#from .views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name = 'login'),
     
]