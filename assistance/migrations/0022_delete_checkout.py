# Generated by Django 4.2.4 on 2023-09-21 02:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("assistance", "0021_remove_equipment_last_maintenance_date_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CheckOut",
        ),
    ]