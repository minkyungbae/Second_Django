from django.urls import path
from . import views

urlpatterns = [
    path('', views.MarketInfoAPIView.as_view()), # market 정보 가져오기
    
]