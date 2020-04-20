from django.db import models

import uuid


class Analytics(models.Model):

    ip_address = models.CharField(max_length=15, unique=True)
    play_time = models.PositiveIntegerField(default=1)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_address
