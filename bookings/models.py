from django.db import models
from django.contrib.auth import get_user_model
from announces.models import Listing

User = get_user_model()


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_soft_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Booking {self.id} for {self.listing.title}'

