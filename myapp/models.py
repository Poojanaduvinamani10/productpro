from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=40)
    price=models.IntegerField()
    quantity= models.IntegerField()
    img=models.ImageField(upload_to='image/')
