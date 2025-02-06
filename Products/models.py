from django.db import models
from SpartaMarkets.models import MarketModel

class ProductModel(models.Model):
    ProductID = models.CharField(max_length=100, primary_key=True) # 상품 ID
    ProductName = models.CharField(max_length=100) # 상품 이름
    ProductPrice = models.IntegerField() # 상품 가격
    Productstock = models.IntegerField() # 상품 재고
    ProductZoneID = models.ForeignKey(
        MarketModel, on_delete=models.CASCADE, related_name="product") # 지점 ID
    
    
