# Generated by Django 4.1.8 on 2023-04-11 14:47

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("visu", "0005_alter_extramenuitem_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="extramenuitem",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="label", unique=True
            ),
        ),
    ]
