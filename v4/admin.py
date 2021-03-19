from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']

admin.site.register(student,StudentAdmin)
