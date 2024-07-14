from django.contrib import admin
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'rooms', 'housing_type', 'is_active', 'is_soft_deleted', 'created_at')
    list_filter = ('is_active', 'is_soft_deleted', 'housing_type', 'created_at')
    search_fields = ('title', 'location', 'description')