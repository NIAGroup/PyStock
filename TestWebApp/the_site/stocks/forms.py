from django import forms
from . import models

class AddNewStock(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ['stock_name', 'stock_symbol']
