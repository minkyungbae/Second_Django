from django.db import models

class CustomerModel(models.Model):
    CustomerID = models.CharField(max_length=100) # 고객 ID
    CustomerName = models.CharField(max_length=50) # 고괙 이름
    CustomerRegDate = models.DateField() # 등록일
    CustomerNumber = models.CharField(max_length=50) # 고객 번호
    
    
