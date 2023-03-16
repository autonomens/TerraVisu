# Generated by Django 4.1.7 on 2023-03-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("visu", "0002_delete_preferences"),
    ]

    operations = [
        migrations.CreateModel(
            name="SpriteValue",
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
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("width", models.PositiveSmallIntegerField()),
                ("height", models.PositiveSmallIntegerField()),
                ("x", models.PositiveSmallIntegerField()),
                ("y", models.PositiveSmallIntegerField()),
                ("pixel_ratio", models.PositiveSmallIntegerField()),
                ("visible", models.BooleanField(default=True)),
            ],
        ),
    ]
