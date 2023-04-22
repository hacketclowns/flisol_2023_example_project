# Generated by Django 4.1.7 on 2023-04-22 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("stores", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("animated", "Animated"),
                            ("adventure", "Adventure"),
                            ("horror", "Horror"),
                            ("adults", "Adults"),
                        ],
                        max_length=9,
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "selled_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="books",
                        to="stores.store",
                    ),
                ),
            ],
        ),
    ]
