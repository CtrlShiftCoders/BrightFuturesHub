from django.db import models
from django.contrib.auth.models import User
from Community.models import Event
from crowdFunding.models import Fund


class UserProfile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    funds_supported = models.ForeignKey(
        Fund, related_name="funds_supported", blank=True, null=True,
        on_delete=models.CASCADE
    )
    funds_created = models.ForeignKey(
        Fund, related_name="funds_created", blank=True, null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user_name}"
