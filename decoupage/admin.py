from django.contrib import admin
from .models import Region, Department, Town


class DepartmentInline(admin.StackedInline):
    model = Department


class TownInline(admin.StackedInline):
    model = Town


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['code_iso', 'code_ansd', 'name', 'area']
    list_filter = ['name']
    search_fields = ['name']
    inlines = [DepartmentInline]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['code_ansd', 'name', 'area', 'region']
    list_filter = ['name']
    search_fields = ['name']
    inlines = [TownInline]


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
    list_filter = ['name']
    search_fields = ['name']
