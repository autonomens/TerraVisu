# Generated by Django 4.1.7 on 2023-04-04 12:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("terra_layer", "0007_rename_create_datetime_scene_created_at_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="scene",
            old_name="baselayer",
            new_name="base_layers",
        ),
    ]
