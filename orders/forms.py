from django import forms
from phonenumber_field.formfields import PhoneNumberField
from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7(777)777-77-77'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Россия, Санкт-Петербург, ул. Мира, дом 6',
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'phone')

