# Generated by Django 4.2.5 on 2023-11-06 11:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("assistance", "0028_remove_equipment_brand_remove_equipment_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="equipment",
            old_name="image",
            new_name="cover",
        ),
    ]
