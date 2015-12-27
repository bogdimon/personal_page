from django.contrib import admin

# Register your models here.
from .models import Skill, Education

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    readonly_fields = ('category',)
    fields = ('category', 'subcategory','name', 'level')
    list_display = ('name', 'level', 'subcategory')
    # list_display_links = ('name')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    readonly_fields = ('category',)
    fields = ('category', 'institution', 'level', 'start_date', 'end_date')
    list_display = ('institution', 'level', 'start_date', 'end_date')
    # list_display_links = ('name')