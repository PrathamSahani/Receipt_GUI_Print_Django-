# Generated by Django 4.2.6 on 2023-10-25 10:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_rename_receipe_receipt"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="receipt",
            name="receipe_view_count",
        ),
    ]
