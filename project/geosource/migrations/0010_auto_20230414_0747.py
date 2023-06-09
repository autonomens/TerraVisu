# Generated by Django 4.1.8 on 2023-04-14 07:47

from django.db import migrations


def migrate_groups(apps, schema_editor):
    Source = apps.get_model("geosource", "Source")
    Group = apps.get_model("auth", "Group")

    for source in Source.objects.all():
        if "groups" in source.settings:
            defined_groups = (
                source.settings.get("groups") or []
            )  # cas where group is null
            for group_id in defined_groups:
                try:
                    group = Group.objects.get(id=group_id)
                    source.groups.add(group)
                except Group.DoesNotExist:
                    pass
            del source.settings["groups"]
            source.save()


def revert_migrate_groups(apps, schema_editor):
    Source = apps.get_model("geosource", "Source")

    for source in Source.objects.all():
        if source.groups.exists():
            source.settings["groups"] = []
            for group in source.groups.all():
                source.settings["groups"].append(group.id)
            source.save()


class Migration(migrations.Migration):
    dependencies = [
        ("geosource", "0009_source_groups"),
    ]

    operations = [
        migrations.RunPython(migrate_groups, revert_migrate_groups),
    ]
