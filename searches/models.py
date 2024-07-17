from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_history')
    query = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Search "{self.query}" by {self.user.username} on {self.searched_at}'
