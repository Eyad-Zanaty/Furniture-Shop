from django import forms
import django_filters
from Home.models import Products

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={"class": "form-control", "id": "search_input", "placeholder": "Search Here", "aria-describedby": "inputGroupPrepend"}))
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Products
        fields = ['name', 'price', 'color']
