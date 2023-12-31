# Generated by Django 4.2.7 on 2023-11-08 20:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ytvideodata",
            name="video_name",
        ),
        migrations.AddField(
            model_name="ytvideodata",
            name="video_subtitle",
            field=models.CharField(default=django.utils.timezone.now, max_length=90),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="ytvideodata",
            name="video_discription",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="ytvideodata",
            name="video_link",
            field=models.CharField(max_length=90),
        ),
    ]
