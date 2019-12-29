from django.contrib import admin
from .models import *
# Register your models here.

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["id","item", "add_time"]

admin.site.register(Favorite, FavoriteAdmin)