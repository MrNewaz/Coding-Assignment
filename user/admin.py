from django.contrib import admin
from .models import *


"""
Advanced admin options:
    - list_display: list of fields to display in the admin list view
    - list_editable: list of fields to edit in the admin list view
    - list_filter: list of fields to filter by in the admin list view
    - list_per_page: number of items to display per page in the admin list view
    - ordering: list of fields to order by in the admin list view
    - search_fields: list of fields to search by in the admin list view
"""


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'street', 'city', 'zip_code']
    list_editable = ['street', 'city', 'zip_code']
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
