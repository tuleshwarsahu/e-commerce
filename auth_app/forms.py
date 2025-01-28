from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ProductFilterForm(forms.Form):
    CATEGORY_CHOICES = [(cat, cat) for cat in Product.objects.values_list('category', flat=True).distinct()]
    category = forms.ChoiceField(choices=[('', 'All Categories')] + CATEGORY_CHOICES, required=False)
    sold = forms.ChoiceField(choices=[('', 'All'), ('True', 'Sold'), ('False', 'Available')], required=False)
    min_price = forms.DecimalField(required=False, label='Min Price')
    max_price = forms.DecimalField(required=False, label='Max Price')
