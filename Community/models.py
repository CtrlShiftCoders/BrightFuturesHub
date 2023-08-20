from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid


class Event(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    event_description = models.TextField()
    type = models.TextField()
    event_duration = models.IntegerField()
    attendees = models.IntegerField(default=0)
    event_date = models.DateField()
    event_start_time = models.TimeField()
    status = models.CharField(max_length=10, default="Upcoming")
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    attendee_details = models.ForeignKey(
        User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"id:{self.id}\n"
            f"title:{self.title}\n"
            f"content:{self.event_description}\n"
            f"type:{self.type}\n"
            f"Attendees:{self.attendees}\n"
            f"Status:{self.status}\n"
            f"Duration:{self.event_duration}\n"
            f"slug:{self.slug}\n"
            )
