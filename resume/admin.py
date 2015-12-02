from django.contrib import admin

# Register your models here.
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    readonly_fields = ('category',)
    fields = ('category', 'subcategory','name', 'level')
    list_display = ('name', 'level', 'subcategory')
    # list_display_links = ('name')