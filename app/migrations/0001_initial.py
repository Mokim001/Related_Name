# Generated by Django 5.1.4 on 2025-03-03 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "sname",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("principal", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("contact", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("sid", models.IntegerField(primary_key=True, serialize=False)),
                ("stdname", models.CharField(max_length=100)),
                ("pno", models.CharField(max_length=100)),
                ("add", models.CharField(max_length=100)),
                (
                    "sname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="app.school",
                    ),
                ),
            ],
        ),
    ]
