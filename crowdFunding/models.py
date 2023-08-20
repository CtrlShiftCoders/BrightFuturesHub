from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid

class Fund(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
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
            f"id:{self.id}\n"
            f"title:{self.title}\n"
            f"content:{self.content}\n"
            f"goal:{self.goal}\n"
            f"Amount Gained:{self.amount_gained}\n"
            f"Status:{self.status}\n"
            f"time:{self.event_datetime}\n"
            f"slug:{self.slug}\n"
            )

