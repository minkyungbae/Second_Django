from django import forms
from .models import ProductModel

class ProductModelForm(forms.ModelForm):
    model = ProductModel
    fields = [
        "product_id",
        "product_name",
        "product_price",
        "product_stock",
        "product_zone_id"
    ]