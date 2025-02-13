from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse

from .models import CustomerModel
from .forms import CustomerModelForm

# 프로필 보기
class CustomerListView(View):
    def get(self, request):
        customers = CustomerModel.objects.all()
        context = {"customers":customers}
        return render(request, "Customers/customerList.html", context)
    
# 프로필 디테일
class CustomerDetailView(View):
    def get(self, request, customer_id):
        customer = get_object_or_404(CustomerModel, customer_id=customer_id)
        return render(request, "Customers/detail.html", {"customer":customer})
        
# customer 정보 가입하기
class CustomerCreateView(View):
    def get(self, request):
        form = CustomerModelForm()
        return render(request, "Customers/create.html", {"form":form})
    
    def post(self, request):
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect(reverse("customer:detail", args=[customer.customer_id]))
        return render(request, "Customers/create.html", {"form":form})
        
        