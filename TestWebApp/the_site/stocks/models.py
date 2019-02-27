from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length=45)
    stock_symbol = models.CharField(max_length=6)
    dates = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock_name

class db_stockInfo(models.Model):
    print("-----------------------------------------")
    dropdwn_choices = []
    for stock in Stock.objects.all():
        #print (stock.stock_symbol)
        dropdwn_choices.append((stock.stock_symbol , stock.stock_symbol))
    dropdwn_choices.sort()
    search_stock_symbol = models.CharField(max_length=6, choices=dropdwn_choices, default='INTL')

    def get_model_fields(model):
        return model._meta.fields
