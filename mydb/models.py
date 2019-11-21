from django.db import models

# Create your models here.
class Article(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    
#Table작성
#만약 모델 바꿀경우 0001_initial.py 지우고 다시 Make migration, Migrate하면 됨.

    
    