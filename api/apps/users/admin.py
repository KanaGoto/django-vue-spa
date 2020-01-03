from django.contrib import admin
from .models import User, Address

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'gender', 'image']
    search_fields = ['username']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','user','first_name','last_name', 'street_address1', 'street_address2', 'city', 'state']
    search_fields = ['user']

#admin.site.register(VerifyCode, VerifyCodeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)

