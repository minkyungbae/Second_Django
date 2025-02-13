from django.urls import path
from . import views

app_name = "spartamarket"
urlpatterns = [
    path('', views.MarketInfoView.as_view(), name="list"), # market list
    path('create/', views.MarketCreateView.as_view(), name="create"), # 마켓 새로 입력하기
    path('detail/<int:market_id>/', views.MarketInfoDetailView.as_view(), name="detail"), # 특정 id 게시물 보기
    path('delete/<int:market_id>/', views.MarketDeleteView.as_view(), name='delete'), # 마켓 삭제하기
    path('update/<int:market_id>/', views.MarketPutView.as_view(), name="update"), # 수정하기
]