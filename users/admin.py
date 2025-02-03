from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for the CustomUser model.
    """
    model = CustomUser

    # Display additional fields in the list view
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')  # Add filters for better navigation

    # Add additional fields in the detail view
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('phone', 'address', 'profile_picture'),
        }),
    )

    # Add additional fields in the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('phone', 'address', 'profile_picture'),
        }),
    )

    # Searchable fields for quick access
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)  # Default ordering by username
