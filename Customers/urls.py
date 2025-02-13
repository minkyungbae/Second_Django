from django.urls import path
from . import views

app_name = "customer"
urlpatterns = [
    path("customerlist/", views.CustomerListView.as_view(), name="customerlist"), # 프로필 리스트 보기
    path("detail/<str:customer_id>/", views.CustomerDetailView.as_view(), name="detail"), # 프로필 디테일
    path("create/", views.CustomerCreateView.as_view(), name="create"), # 생성하기
    path("update/<str:customer_id>/", views.CustomerUpdateView.as_view(), name="update"), # 수정하기
    path("delete/<str:customer_id>/", views.CustomerDeleteView.as_view(), name="delete"), # 삭제하기
]