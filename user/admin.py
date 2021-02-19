from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from user.models import User


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'first_name', 'last_name', 'password1', 'password2', 'balance', 'phone_number',),
        }),
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'balance')
    ordering = ['email']