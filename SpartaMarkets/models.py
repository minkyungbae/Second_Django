from django.db import models

class MarketModel(models.Model):
    market_id = models.CharField(max_length=50)  # 지점 ID
    market_zone = models.CharField(max_length=300)  # 지점 지역
    market_manager = models.CharField(max_length=50)  # 지점장 이름
    market_number = models.CharField(max_length=50)  # 지점 전화번호
    market_opening_date = models.DateField(auto_now_add=True)  # 개점 날짜
    market_employees = models.IntegerField()  # 직원 수
    
