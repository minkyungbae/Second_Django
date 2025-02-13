from django import forms
from .models import CustomerModel

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = "__all__"
        exclude = ("customer_regdate",)
        
        
class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = "__all__"
        exclude = ("customer_regdate","customer_id",)