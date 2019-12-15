import xadmin
from .models import Reviews

class ReviewsAdmin(object):
    list_display = ["prod", "user", "star", "title", "comment", "add_time"]

xadmin.site.register(Reviews, ReviewsAdmin)
