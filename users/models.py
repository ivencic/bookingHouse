"""from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    announces = models.ForeignKey(default=False, on_delete=models.CASCADE)
    bookings = models.ForeignKey(default=False, on_delete=models.CASCADE)
    reviews = models.ForeignKey(default=False, on_delete=models.CASCADE)
    ratings = models.ForeignKey(default=False, on_delete=models.CASCADE)
    email = unique=True
    
"""

