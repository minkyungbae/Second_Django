from django.urls import path
from . import views

urlpatterns = [
    path('', views.MarketInfoAPIView.as_view()), # market 정보 가져오기
    path('<int:market_id>/', views.MarketInfoAPIView.as_view()), # 특정 market 정보 가져오기
    
]