from django.urls import path
from . import views

urlpatterns = [
    path('', views.MarketInfoAPIView.as_view()), # market list
    path('<int:market_id/', views.MarketInfoDetailAPIView.as_view()) # 특정 id 게시물 목록 조회, 삭제 및 수정
]