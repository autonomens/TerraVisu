# Generated by Django 4.1.7 on 2023-03-15 15:54

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geosource", "0007_alter_source_report"),
    ]

    operations = [
        migrations.AlterField(
            model_name="field",
            name="sample",
            field=models.JSONField(
                blank=True,
                default=list,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
            ),
        ),
    ]
