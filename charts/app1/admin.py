from django.contrib import admin
from .models import Country, Year, SuicideCase

admin.site.register(Country)

admin.site.register(Year)

#admin.site.register(SuicideCase)

@admin.register(SuicideCase)
class AdminSuicideClass(admin.ModelAdmin):
    list_display = ['country','year','case']
    
