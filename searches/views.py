from rest_framework import generics, permissions
from .models import SearchHistory
from .serializers import SearchHistorySerializer


class SearchHistoryListCreateView(generics.ListCreateAPIView):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
