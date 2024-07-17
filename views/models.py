from django.db import models
from django.contrib.auth import get_user_model
from announces.models import Listing

User = get_user_model()


class ListingViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='view_history')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='view_history')
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} viewed {self.listing.title} on {self.viewed_at}'