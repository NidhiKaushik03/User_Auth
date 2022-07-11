from django.contrib import admin
from .models import Emp_Info

# Register your models here.


class Emp_InfotAdmin(admin.ModelAdmin):
    list_display = ("Fullname", "Salary", "Address", "Status")

admin.site.register(Emp_Info,Emp_InfotAdmin)


