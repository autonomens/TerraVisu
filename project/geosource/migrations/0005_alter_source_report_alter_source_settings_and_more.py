# Generated by Django 4.1.4 on 2022-12-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("geosource", "0004_alter_source_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="source",
            name="report",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="source",
            name="settings",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="source",
            name="task_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="source",
            name="task_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
