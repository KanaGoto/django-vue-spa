from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = ['username']

#admin.site.register(VerifyCode, VerifyCodeAdmin)
admin.site.register(Account, AccountAdmin)