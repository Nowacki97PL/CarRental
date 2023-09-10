from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from datetime import datetime

from .models import Car, RentalTerms, CompanyBranches, Rent


class RentCreateViewTest(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username="testuser", password="testpass"
        )
        self.car = Car.objects.create(
            brand="TestBrand",
            model="TestModel",
            cars_type="SomeType",
            capacity=1.58,
            year="2023",
            number_of_seats=4,
            consumption="SomeCons",
            power="SomePower",
            car_mileage="SomeMil",
            transmission="So",
            no_gears="SomeG",
            drive="Some",
        )
        self.rental_terms = RentalTerms.objects.create(car=self.car, price=100)
        self.company_branch = CompanyBranches.objects.create(city="TestCity")

        self.start_date = datetime(2023, 9, 1)
        self.end_date = datetime(2023, 9, 10)

    def test_car_available(self):
        rent = Rent(
            rental_terms=self.rental_terms,
            start_date=self.start_date,
            end_date=self.end_date,
        )
        self.assertTrue(rent.is_car_available())

    def test_car_unavailable(self):
        company_branch = CompanyBranches.objects.create(city="Test City")
        Rent.objects.create(
            rental_terms=self.rental_terms,
            client=self.user,
            start_date=self.start_date,
            end_date=self.end_date,
            take_from=self.company_branch,
            take_back=self.company_branch,
        )
        rent = Rent(
            rental_terms=self.rental_terms,
            client=self.user,
            start_date=self.start_date,
            end_date=self.end_date,
            take_from=company_branch,
            take_back=company_branch,
        )

        self.assertFalse(rent.is_car_available())

    def test_rental_creation_when_proper_data(self):
        self.client.login(username="testuser", password="testpass")

        data = {
            "rental_terms": self.rental_terms.id,
            "start_date": "2023-09-01",
            "end_date": "2023-09-10",
            "take_from": self.company_branch.id,
            "take_back": self.company_branch.id,
        }

        response = self.client.post(
            reverse("create_rent", kwargs={"car_id": self.car.id}), data
        )

        self.assertRedirects(response, reverse("confirm_reservation", kwargs={"id": 1}))
        self.assertTrue(Rent.objects.filter(rental_terms=self.rental_terms).exists())

    def test_form_invalid_data(self):
        self.client.login(username="testuser", password="testpass")

        data = {
            "rental_terms": self.rental_terms.id,
            "start_date": "2023-09-10",
            "end_date": "2023-09-01",
            "take_from": self.company_branch.id,
            "take_back": self.company_branch.id,
        }

        response = self.client.post(
            reverse("create_rent", kwargs={"car_id": self.car.id}), data
        )

        self.assertFalse(response.context["form"].is_valid())
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Rent.objects.filter(rental_terms=self.rental_terms).exists())
        
    def test_rent_same_car_at_the_same_time(self):
        self.client.login(username="testuser", password="testpass")

        data_1 = {
            "rental_terms": self.rental_terms.id,
            "start_date": "2023-09-01",
            "end_date": "2023-09-10",
            "take_from": self.company_branch.id,
            "take_back": self.company_branch.id,
        }

        response_1 = self.client.post(
            reverse("create_rent", kwargs={"car_id": self.car.id}), data_1
        )
        self.assertRedirects(response_1, reverse("confirm_reservation", kwargs={"id": 1}))
        self.assertTrue(Rent.objects.filter(rental_terms=self.rental_terms).exists())

        data_2 = {
            "rental_terms": self.rental_terms.id,
            "start_date": "2023-09-01",
            "end_date": "2023-09-10",
            "take_from": self.company_branch.id,
            "take_back": self.company_branch.id,
        }

        response_2 = self.client.post(
            reverse("create_rent", kwargs={"car_id": self.car.id}), data_2
        )

        self.assertFalse(response_2.context["form"].is_valid())
        self.assertEqual(response_2.status_code, 200)
        self.assertTrue(Rent.objects.filter(rental_terms=self.rental_terms).count(), 1)
        
        
class RentalTermsCreateViewTests(TestCase):
    def test_create_rental_terms_with_no_data(self):
        self.client.login(username="testuser", password="testpass")
        data = {}
        response = self.client.post(reverse("create_rental_terms"), data)
        self.assertFalse(response.context["form"].is_valid())
        self.assertEqual(response.status_code, 200)
        self.assertFalse(RentalTerms.objects.exists())

    def test_create_rental_terms_with_invalid_price(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "price": "invalid_price",
        }
        response = self.client.post(reverse("create_rental_terms"), data)
        self.assertFalse(response.context["form"].is_valid())
        self.assertEqual(response.status_code, 200)
        self.assertFalse(RentalTerms.objects.exists())

    def test_create_rental_terms_with_empty_price(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "price": "",
        }
        response = self.client.post(reverse("create_rental_terms"), data)
        self.assertFalse(response.context["form"].is_valid())
        self.assertEqual(response.status_code, 200)
        self.assertFalse(RentalTerms.objects.exists())
        