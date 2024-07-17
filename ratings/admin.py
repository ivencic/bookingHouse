from django.contrib import admin
from .models import Rating


@admin.register(Rating)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('listing', 'booking', 'user', 'rating', 'created_at', 'updated_at')

