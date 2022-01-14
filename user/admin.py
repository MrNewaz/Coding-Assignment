from django.contrib import admin
from .models import *


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'street', 'city']
    list_editable = ['street']
    list_filter = ['first_name', 'last_name']
    list_per_page = 10
    ordering = ['first_name']
    search_fields = ['first_name__startswith']


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'parent']
    list_filter = ['first_name', 'last_name']
    list_per_page = 10
    ordering = ['first_name']
    search_fields = ['first_name__startswith']
