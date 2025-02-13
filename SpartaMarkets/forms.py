from django import forms
from .models import MarketModel

class MarketModelForm(forms.ModelForm):
    class Meta:
        model = MarketModel
        fields = [
            "market_id",
            "market_zone",
            "market_manager",
            "market_number",
            "market_employees",
            ]
        exclude = ("market_opening_date",)