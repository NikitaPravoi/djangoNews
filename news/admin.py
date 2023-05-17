from django.contrib import admin
from .models import Event, Project, Work, News

admin.site.register(Project)
admin.site.register(Work)
admin.site.register(News)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'publish']
    list_filter = ['created', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'title': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']


