from django.shortcuts import render,redirect
from .models import Stock
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.http import JsonResponse
from .STOCK_DATA_GRAB import grab_stock_points
import datetime, timestring
# Create your views here.

def stocks_list(request):
    #sorts the objects in the database
    if request.method == "POST":
        form = forms.AddNewStock(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stocks:stocks')
    else:
        form = forms.AddNewStock()
    stocks = Stock.objects.all().order_by('dates')
    return render(request,"stocks/stocks_list.html", {'Stocks': stocks,'form':form})

def AddStock(request):
    if request.method == "POST":
        form = forms.AddNewStock(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stocks:stocks')
    else:
        form = forms.AddNewStock()
    '''if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stocks:stocks')
    else:
        form = UserCreationForm()'''
    #return(request,"stocks/stock_create.html",{'form':form})
    return render(request,"stocks/stock_create.html",{'form':form})

def get_LeData(request,*args,**kwargs):
    '''data = {
        "val1": 100,
        "val2": 200,
    }'''
    chart_labels = []
    chart_points = []
    data = grab_stock_points()
    data_points = {"points":[]}
    for s in data:
        data_point = {"date":str(s), "value":str(data[s]["SMA"])}

        #date = datetime.datetime.strptime(str(s),'%y%m%d')
        date = timestring.Date(str(s)).date
        date = datetime.datetime.strftime(date,'%m-%d-%y')
        chart_labels.append(str(date))
        chart_points.append(str(data[s]["SMA"]))
        data_points["points"].append(data_point)
    data_points = {
    "stock_name":"Intel Corp. : INTL",
    "dates":chart_labels[::-1],
    "values":chart_points[::-1],
    }
    return JsonResponse(data_points)
    #return JsonResponse(data)
