from django import forms


from .models import Car, CompanyBranches, Rent, RentalTerms, UserProfile


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "avatar": forms.ClearableFileInput(
                attrs={"class": "form-control is_valid"}
            ),
            "brand": forms.TextInput(attrs={"class": "form-control is_valid"}),
            "model": forms.TextInput(attrs={"class": "form-control is_valid"}),
            "cars_type": forms.Select(attrs={"class": "form-control is_valid"}),
            "engine": forms.Select(attrs={"class": "form-control is_valid"}),
            "capacity": forms.NumberInput(attrs={"class": "form-control is_valid"}),
            "year": forms.TextInput(attrs={"class": "form-control is_valid"}),
            "number_of_seats": forms.NumberInput(
                attrs={"class": "form-control is_valid"}
            ),
            "consumption": forms.TextInput(attrs={"class": "form-control is_valid"}),
            "power": forms.TextInput(attrs={"class": "form-control is_valid"}),
            "car_mileage": forms.TextInput(attrs={"class": "form-control is_valid"}),
            "transmission": forms.Select(attrs={"class": "form-control is_valid"}),
            "no_gears": forms.Select(attrs={"class": "form-control is_valid"}),
            "drive": forms.Select(attrs={"class": "form-control is_valid"}),
        }
        
        labels = {
            "avatar": "Zdjęcie",
            "brand": "Marka",
            "model": "Model",
            "cars_type": "Typ nadwozia",
            "engine": "Silnik",
            "capacity": "Pojemność",
            "year": "Rok produkcji",
            "number_of_seats": "Ilość miejsc",
            "consumption": "Spalanie",
            "power": "Moc silnika",
            "car_mileage": "Przebieg",
            "transmission": "Skrzynia biegów",
            "no_gears": "Ilość biegów",
            "drive": "Typ napędu",
        }
        



class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ["rental_terms", "start_date", "end_date", "take_from", "take_back"]
        widgets = {
            "rental_terms": forms.Select(attrs={"class": "form-select is_valid"}),
            "start_date": forms.DateInput(
                attrs={"class": "form-control is_valid", "type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"class": "form-control is_valid", "type": "date"}
            ),
            "take_from": forms.Select(attrs={"class": "form-select is_valid"}),
            "take_back": forms.Select(attrs={"class": "form-select is_valid"}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar", "phone", "first_name", "last_name"]
        widgets = {
            "avatar": forms.ClearableFileInput(
                attrs={"class": "form-control is_valid"}
            ),
            "phone": forms.TextInput(attrs={"class": "form-control is_valid"}),
            "first_name": forms.TextInput(attrs={"class": "form-control is_valid"}),
            "last_name": forms.TextInput(attrs={"class": "form-control is_valid"}),
        }
        labels = {
            "avatar": "Zdjęcie",
            "phone": "Telefon",
            "first_name": "Imię",
            "last_name": "Nazwisko",
        }


class DeleteCarForm(forms.Form):
    car_id = forms.ModelChoiceField(
        queryset=Car.objects.all(),
        label="Wybierz pojazd do usunięcia",
        widget=forms.Select(attrs={"class": "form-control is_valid"}),
    )


class EditCarForm(forms.Form):
    car_id = forms.ModelChoiceField(
        queryset=Car.objects.all(),
        label="Wybierz pojazd do edycji",
        widget=forms.Select(attrs={"class": "form-control is_valid"}),
    )
    
class RentalTermsForm(forms.ModelForm):
    class Meta:
        model = RentalTerms
        fields = ["car", "price"]


class CompanyBranchesForm(forms.ModelForm):
    class Meta:
        model = CompanyBranches
        fields = ["city"]
        widget={"city":forms.TextInput(attrs={"class": 'form-control is valid'})},
        
        labels = {
            "city": "Miasto",
        }
