from django import forms
from .models import CustomerModel

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = [
            "customer_id",
            "customer_name",
            "customer_number",
            ]
        exclude = ("customer_regdate",)