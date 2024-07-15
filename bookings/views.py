from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsOwnerOrReadOnly, IsListingOwnerOrReadOnly


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly, IsListingOwnerOrReadOnly]

    def get_object(self):
        booking = super().get_object()
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if not booking.listing.owner == self.request.user and not booking.user == self.request.user:
                raise PermissionDenied("You do not have permission to edit or delete this booking.")
        return booking

    def perform_update(self, serializer):
        booking = self.get_object()
        if 'is_confirmed' in self.request.data and booking.listing.owner != self.request.user:
            raise PermissionDenied("Only the listing owner can change the confirmation status.")
        serializer.save()
