from django.contrib import admin
from .models import DataEntry

class DataEntryAdmin(admin.ModelAdmin):
    list_display = ['intensity', 'likelihood', 'relevance', 'country', 'topics', 'region', 'city', 'end_year', 'start_year', 'insight', 'url', 'impact', 'added', 'published', 'pestle', 'source', 'title']
    list_filter = ['region', 'pestle', 'source']  # Add 'region', 'pestle', and 'source' fields for filtering

admin.site.register(DataEntry, DataEntryAdmin)
