from django.contrib import admin

from images.models import Category, Image, Location
from .views import *
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
  search_fields = ['category__name']


admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)