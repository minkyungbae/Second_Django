from django.db import models

class CustomerModel(models.Model):
    customer_id = models.CharField(max_length=100, primary_key=True) # 고객 ID
    customer_name = models.CharField(max_length=50) # 고괙 이름
    customer_regdate = models.DateField(auto_now_add=True) # 등록일
    customer_number = models.CharField(max_length=50) # 고객 번호
