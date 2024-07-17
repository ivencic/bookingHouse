from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('listing', 'user', 'start_date', 'end_date', 'is_confirmed', 'created_at')
