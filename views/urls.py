from django.urls import path
from .views import ListingViewHistoryListCreateView

urlpatterns = [
    path('view-history/', ListingViewHistoryListCreateView.as_view(), name='view-history'),
]