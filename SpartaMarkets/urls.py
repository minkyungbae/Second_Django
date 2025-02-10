from django.urls import path
from . import views

app_name = "spartamarket"
urlpatterns = [
    path('', views.MarketInfoView.as_view(), name="market_list"), # market list
    path('<int:market_id/', views.MarketInfoDetailView.as_view, name="detail") # 특정 id 게시물 목록 조회, 삭제 및 수정
]