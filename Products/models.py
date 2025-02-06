from django.db import models
from SpartaMarkets.models import MarketModel

class ProductModel(models.Model):
    product_id = models.CharField(max_length=100, primary_key=True) # 상품 ID
    product_name = models.CharField(max_length=100) # 상품 이름
    product_price = models.IntegerField() # 상품 가격
    product_stock = models.IntegerField() # 상품 재고
    product_zone_id = models.ForeignKey(
        MarketModel, on_delete=models.CASCADE, related_name="product") # 지점 ID
    
    
