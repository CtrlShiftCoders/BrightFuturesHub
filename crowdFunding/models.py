from django.db import models
from django.utils.text import slugify
import uuid 

class Fund(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    goal = models.IntegerField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"id:{self.id},"
            f"title:{self.title},"
            f"content:{self.content},"
            f"goal:{self.goal},"
            f"slug:{self.slug}"
            )

