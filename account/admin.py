import imp
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel

# Register your models here.
@admin.register(CustomUserModel)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (

        ( 'Avatar dəyişmə ',{'fields':['avatar']}) ,
    )
