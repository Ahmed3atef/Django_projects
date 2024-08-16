from django.contrib.gis.admin import GISModelAdmin
from django.contrib import admin
from shops.models import Shop

@admin.register(Shop)
class ShopAdmin(GISModelAdmin):
    list_display = ('name', 'location')

