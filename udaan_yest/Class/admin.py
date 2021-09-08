from django.contrib import admin
from django.db import models
from .models import Class
# Register your models here.
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    
    list_display=('type',)