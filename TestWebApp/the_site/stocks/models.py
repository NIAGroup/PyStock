from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length=25)
    stock_symbol = models.CharField(max_length=6)
    dates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock_name
