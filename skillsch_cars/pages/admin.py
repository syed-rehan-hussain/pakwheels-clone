from django.contrib import admin
from django.utils.html import format_html
from .models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius:4px;" width="40px" />'.format(object.image.url))
    list_display = ('id' , 'thumbnail' , 'firstName' , 'lastName' , 'designation' , 'date')
    list_display_links = ('id','firstName',)
    search_fields = ('firstName' , 'designation')
    list_filter = ('designation',)

admin.site.register(Team,TeamAdmin)
