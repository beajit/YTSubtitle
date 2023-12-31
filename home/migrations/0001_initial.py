# Generated by Django 4.2.7 on 2023-11-07 20:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="YtVideoData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "updated_on",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Modification Date"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation Date"
                    ),
                ),
                ("is_delete", models.BooleanField(default=False)),
                (
                    "video_link",
                    models.CharField(max_length=90, verbose_name="Question"),
                ),
                (
                    "video_discription",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "video_name",
                    models.CharField(max_length=90, verbose_name="Question"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("", "--Select Status--"),
                            ("IN_ACTIVE", "In-Active"),
                            ("DRAFT", "Draft"),
                            ("PUBLISHED", "Published"),
                            ("DEMO", "Demo"),
                        ],
                        default="PUBLISHED",
                        max_length=300,
                        verbose_name="Status",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
