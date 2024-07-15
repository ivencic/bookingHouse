from rest_framework import serializers
from .models import Booking
from datetime import date


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user']

    def validate_start_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("The start date cannot be earlier than today.")
        return value

    def validate(self, data):
        """
        Check that the start and end dates do not overlap with existing bookings.
        """
        listing = data['listing']
        start_date = data['start_date']
        end_date = data['end_date']

        # Check for overlapping bookings
        overlapping_bookings = Booking.objects.filter(
            listing=listing,
            start_date__lt=end_date,
            end_date__gt=start_date,
            is_soft_deleted=False
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError("The selected date range is not available.")

        return data
