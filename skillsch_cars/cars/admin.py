from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class Caradmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius:4px;" width="40px" />'.format(object.carphoto.url))
    list_display = ('id','thumbnail','car_title','price','year','model','city','is_featured')
    list_display_links = ('id','car_title')
    search_fields = ('car_title', 'model','year')
    list_editable = ('is_featured',)
    list_filter = ('model','city')

admin.site.register(Car,Caradmin)
