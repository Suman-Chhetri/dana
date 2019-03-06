from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'password', 'first_name', 'last_name', 'is_staff', 'role']



admin.site.register(CustomUser)
