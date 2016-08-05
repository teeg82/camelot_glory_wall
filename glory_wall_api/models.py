from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class UtopiaMessageSummary(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)

    message_text = models.TextField(null=False, blank=False)
    
    received_at = models.DateTimeField(null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.received_at:
            self.received_at = timezone.now()
        return super(UtopiaMessageSummary, self).save(*args, **kwargs)