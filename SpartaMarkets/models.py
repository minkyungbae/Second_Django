from django.db import models

class MarketModel(models.Model):
    MarketID = models.CharField(max_length=50) # 지점ID
    MarketZone = models.TextField(max_length=300) # 지점 지역
    MarketManager = models.TextField(max_length=50) # 지점장 이름
    MarketNumber = models.TextField(max_length=50) # 지점 번호
    MarketOpeningDate = models.DateField(auto_now_add=True) # 개점 날짜
    MarketEmployees = models.IntegerField(max_length=50) # 직원 수
    
