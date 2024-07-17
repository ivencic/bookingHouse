from rest_framework import serializers
from .models import ListingViewHistory


class ListingViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingViewHistory
        fields = ['id', 'user', 'listing', 'viewed_at']
