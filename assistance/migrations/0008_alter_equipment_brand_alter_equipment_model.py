# Generated by Django 4.2.4 on 2023-08-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assistance", "0007_equipment_description_alter_equipment_model_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="brand",
            field=models.CharField(
                choices=[("athletic", "Athletic")], default="athletic", max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="equipment",
            name="model",
            field=models.CharField(max_length=200),
        ),
    ]
