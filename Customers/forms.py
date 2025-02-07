from django import forms
from .models import CustomerModel

class CustomerModelForm(forms.ModelForm):
    model = CustomerModel
    fields = [
        "customer_id",
        "customer_name",
        "customer_regdate",
        "customer_number",
    ]