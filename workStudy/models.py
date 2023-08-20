from django.db import models
from django.utils.text import slugify

class Jobs(models.Model):
        job_id = models.IntegerField(primary_key=True)
        job_name = models.CharField(max_length=30,unique=True)
        job_description = models.TextField()
        payment = models.FloatField()
        job_duration = models.IntegerField()
        start_date = models.DateField()
        image = models.CharField(max_length=200)
        job_category = models.CharField(max_length=30)
        type = models.CharField(max_length=30)
        job_slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
            self.slug = slugify(self.job_name)
            super().save(*args, **kwargs)

        def __str__(self):
            return (
                    f"job_id:{self.job_id}\n"
                    f"job_name:{self.job_name}\n"
                    f"job_description:{self.job_description}\n"
                    f"payment:{self.payment}\n"
                    f"job_duration:{self.payment}\n"
                    f"start_date:{self.start_date}\n"
                    f"image:{self.image}\n"
                    f"job_category:{self.job_category}\n"
                    f"type:{self.type}\n"
                    f"job_slug:{self.job_slug}\n"
                    )
