# Generated by Django 4.2.4 on 2023-08-26 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppRentCar", "0008_alter_car_cars_type_alter_car_drive_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rentalterms",
            name="price",
        ),
        migrations.AddField(
            model_name="rentalterms",
            name="premium_price",
            field=models.DecimalField(decimal_places=2, max_digits=16, null=True),
        ),
        migrations.AddField(
            model_name="rentalterms",
            name="regular_price",
            field=models.DecimalField(decimal_places=2, max_digits=16, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="rentals_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="car",
            name="cars_type",
            field=models.CharField(
                choices=[
                    ("Kombi", "Kombi"),
                    ("Sedan", "Sedan"),
                    ("Coupe", "Coupe"),
                    ("Suv", "Suv"),
                    ("Van", "Van"),
                    ("Hatchback", "Hatchback"),
                    ("Shooting brake", "Shooting brake"),
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
                    ("Benzyna", "Benzyna"),
                    ("Diesel", "Diesel"),
                    ("Hybryda", "Hybryda"),
                    ("Elektryczny", "Elektryczny"),
                ],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="no_gears",
            field=models.CharField(
                choices=[("7", "7"), ("6", "6"), ("8", "8"), ("5", "5")], max_length=8
            ),
        ),
    ]
