from django.db import models
from django.contrib.auth import get_user_model
from announces.models import Listing
from bookings.models import Booking

User = get_user_model()


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review for {self.listing.title} by {self.user.username}'

    class Meta:
        unique_together = ['listing', 'booking', 'user']
