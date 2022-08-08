import imp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUserModel

    fieldsets = UserAdmin.fieldsets + (

        ( 'Avatar dəyişmə ',{'fields':['avatar']}) ,
    )

admin.site.register(CustomUserModel,CustomUserAdmin)