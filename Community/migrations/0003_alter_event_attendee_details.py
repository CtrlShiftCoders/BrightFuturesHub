# Generated by Django 4.2.4 on 2023-08-20 11:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Community", "0002_remove_event_attendee_details_event_attendee_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="attendee_details",
            field=models.ManyToManyField(
                blank=True, related_name="attendees", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]