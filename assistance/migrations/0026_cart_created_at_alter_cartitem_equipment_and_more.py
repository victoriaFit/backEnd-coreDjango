# Generated by Django 4.2.5 on 2023-10-13 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("assistance", "0025_remove_cart_created_at_alter_cartitem_equipment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),

        migrations.AlterField(
            model_name="cartitem",
            name="equipment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="assistance.equipment",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="assistance.item",
            ),
        ),
    ]