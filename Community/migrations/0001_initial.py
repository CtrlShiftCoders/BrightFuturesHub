# Generated by Django 4.2.4 on 2023-08-20 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("event_description", models.TextField()),
                ("type", models.TextField()),
                ("event_duration", models.IntegerField()),
                ("attendees", models.IntegerField(default=0)),
                ("event_date", models.DateField()),
                ("event_start_time", models.TimeField()),
                ("status", models.CharField(default="Upcoming", max_length=10)),
                ("slug", models.SlugField(unique=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "attendee_details",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendees",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organiser",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
