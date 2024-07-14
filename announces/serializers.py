from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price', 'rooms', 'housing_type', 'is_active', 'views', 'created_at', 'updated_at', 'is_soft_deleted']
        read_only_fields = ['owner']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if instance.owner != request.user and not request.user.is_staff:
            raise serializers.ValidationError("You do not have permission to edit this listing.")
        return super().update(instance, validated_data)
