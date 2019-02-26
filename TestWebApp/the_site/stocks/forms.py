from django import forms
from . import models
from . import views

class AddNewStock(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ['stock_name', 'stock_symbol']

class goForIT(forms.ModelForm):
    class Meta:
        model = models.db_stockInfo
        fields = ['search_stock_symbol']
