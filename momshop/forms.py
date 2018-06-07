from django import forms
from .models import Products


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30)

class CartForm(forms.Form):

    class Meta:
        model = Products
        fields = ['title', 'price']