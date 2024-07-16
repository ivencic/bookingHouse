from rest_framework import serializers

from bookings.models import Booking
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def validate(self, data):
        """
        Check that the user has at least one booking for the listing.
        """
        user = self.context['request'].user
        if not Booking.objects.filter(listing=data['listing'], user=user).exists():
            raise serializers.ValidationError("You must have at least one booking for this listing to rate it.")
        return data
