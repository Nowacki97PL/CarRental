# Generated by Django 4.2.4 on 2023-09-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "AppRentCar",
            "0020_alter_car_cars_type_alter_car_drive_alter_car_engine_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="cars_type",
            field=models.CharField(
                choices=[
                    ("Hatchback", "Hatchback"),
                    ("Shooting brake", "Shooting brake"),
                    ("Van", "Van"),
                    ("Sedan", "Sedan"),
                    ("Coupe", "Coupe"),
                    ("Kombi", "Kombi"),
                    ("Suv", "Suv"),
                    ("Cabrio", "Cabrio"),
                ],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="drive",
            field=models.CharField(
                choices=[("4x4", "4x4"), ("Przedni", "Przedni"), ("Tylni", "Tylni")],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="engine",
            field=models.CharField(
                choices=[
                    ("Hybryda", "Hybryda"),
                    ("Benzyna", "Benzyna"),
                    ("Diesel", "Diesel"),
                    ("Elektryczny", "Elektryczny"),
                ],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="no_gears",
            field=models.CharField(
                choices=[("8", "8"), ("5", "5"), ("7", "7"), ("6", "6")], max_length=8
            ),
        ),
    ]