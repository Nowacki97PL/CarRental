# Generated by Django 4.2.4 on 2023-08-20 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("AppRentCar", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rent",
            old_name="car",
            new_name="rental_terms",
        ),
        migrations.RenameField(
            model_name="rentalterms",
            old_name="car_id",
            new_name="car",
        ),
        migrations.AlterField(
            model_name="car",
            name="cars_type",
            field=models.CharField(
                choices=[
                    ("Suv", "Suv"),
                    ("Kombi", "Kombi"),
                    ("Sedan", "Sedan"),
                    ("Hatchback", "Hatchback"),
                    ("Shooting brake", "Shooting brake"),
                    ("Van", "Van"),
                    ("Coupe", "Coupe"),
                ],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="drive",
            field=models.CharField(
                choices=[("4x4", "4x4"), ("Tylni", "Tylni"), ("Przedni", "Przedni")],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="engine",
            field=models.CharField(
                choices=[
                    ("Hybryda", "Hybryda"),
                    ("Elektryczny", "Elektryczny"),
                    ("Diesel", "Diesel"),
                    ("Benzyna", "Benzyna"),
                ],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="no_gears",
            field=models.CharField(
                choices=[("5", "5"), ("7", "7"), ("6", "6"), ("8", "8")], max_length=8
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="transmission",
            field=models.CharField(
                choices=[("Automatyczna", "Automatyczna"), ("Manuala", "Manualna")],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="rent",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
