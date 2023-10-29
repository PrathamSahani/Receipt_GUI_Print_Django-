# Generated by Django 4.2.6 on 2023-10-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="receipe",
            name="receipe_description",
        ),
        migrations.RemoveField(
            model_name="receipe",
            name="receipe_name",
        ),
        migrations.AddField(
            model_name="receipe",
            name="price",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="receipe",
            name="quantity",
            field=models.IntegerField(default=0),
        ),
    ]