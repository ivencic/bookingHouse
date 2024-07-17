from rest_framework import generics, permissions
from .models import ListingViewHistory
from .serializers import ListingViewHistorySerializer


class ListingViewHistoryListCreateView(generics.ListCreateAPIView):
    queryset = ListingViewHistory.objects.all()
    serializer_class = ListingViewHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)