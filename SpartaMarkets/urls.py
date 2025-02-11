from django.urls import path
from . import views

app_name = "spartamarket"
urlpatterns = [
    path('', views.MarketInfoView.as_view(), name="market-list"), # market list
    path('/create/', views.MarketCreateView.as_view(), name="create-market"), # 마켓 새로 입력하기
    path('<int:market_id/', views.MarketInfoDetailView.as_view, name="detail") # 특정 id 게시물 목록 조회, 삭제 및 수정
]