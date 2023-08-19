from django.db import models
from django.utils.text import slugify
import uuid

from django.utils import timezone 

class Fund(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    goal = models.IntegerField()
    amount_gained = models.IntegerField(default=0)
    status= models.CharField(max_length=10,default="In Progress")
    slug = models.SlugField(unique=True)
    event_datetime=models.DateTimeField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"id:{self.id},"
            f"title:{self.title},"
            f"content:{self.content},"
            f"goal:{self.goal},"
            f"Amount Gained:{self.amount_gained},"
            f"Status:{self.status},"
            f"time:{self.event_datetime},"
            f"slug:{self.slug}"
            )

