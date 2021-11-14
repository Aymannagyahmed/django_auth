from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class MyCustomUser(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password','job')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),)

admin.site.register( User,MyCustomUser )

