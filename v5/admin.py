from django.contrib import admin
from .models import student
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','city','roll']
    search_fields=['name','roll']
    
admin.site.register(student,studentAdmin)
