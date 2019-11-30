from django.contrib import admin
from .models import Reviews
# Register your models here.

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ["prod", "user", "star", "title", "comment", "add_time"]

admin.site.register(Reviews, ReviewsAdmin)

