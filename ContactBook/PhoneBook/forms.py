from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}), label="Ім'я")
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}), label="Прізвище")
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-control"}), label="Номер телефону")
    email = forms.EmailField(required=False, max_length=100, widget=forms.EmailInput(attrs={"class": "form-control"}), label="Email")
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control", "rows": 3}), label="Адреса")
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={"class": "form-control"}), label="Aватарка")


    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone_number", "email", "address", "profile_picture",)
