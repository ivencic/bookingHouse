from django.db import models
from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer
from .permissions import IsAdminOrOwnerOrReadOnly
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated


class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.filter(is_soft_deleted=False)
    serializer_class = ListingSerializer
    permission_classes = [IsAdminOrOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.filter(is_soft_deleted=False)
    serializer_class = ListingSerializer
    permission_classes = [IsAdminOrOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Listing.objects.none()
        return Listing.objects.filter(models.Q(is_active=True) | models.Q(owner=user)).filter(is_soft_deleted=False)

    def perform_destroy(self, instance):
        instance.is_soft_deleted = True
        instance.save()


class PopularListingsView(generics.ListAPIView):
    queryset = Listing.objects.annotate(
        review_count=Count('reviews')
    ).order_by('-views', '-review_count')
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]