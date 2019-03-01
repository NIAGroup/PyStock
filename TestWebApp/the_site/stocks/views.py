from django.shortcuts import render,redirect
from .models import Stock,db_stockInfo
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.http import JsonResponse
from .STOCK_DATA_GRAB import grab_stock_points
import datetime, timestring, operator, pyrebase, json
# Create your views here.
config = {
    'apiKey': "AIzaSyDPFA_o-J2dVwaRuEKaKmR9vMpBnpdXZIQ",
    'authDomain': "nia-webapp-project.firebaseapp.com",
    'databaseURL': "https://nia-webapp-project.firebaseio.com",
    'projectId': "nia-webapp-project",
    'storageBucket': "nia-webapp-project.appspot.com",
    'messagingSenderId': "385434752039"
}
firebase = pyrebase.initialize_app(config)
firebase_auth = firebase.auth()
firebase_db = firebase.database()

def stocks_list(request):
    #sorts the objects in the database
    if request.method == "POST":
        form_A = forms.AddNewStock(request.POST)
        print('running in stocks_list if')
        form_B = forms.goForIT()
        if form_A.is_valid():
            form_A.save()
            return redirect('stocks:stocks')
    else:
        form_A = forms.AddNewStock()
        print("running in stocks_list else")
        form_B = forms.goForIT()
    stocks = Stock.objects.all().order_by('stock_name')
    arr = list(stocks.values())
    for stock in arr:
        print(stock)
        for s in stock:
            #print(str(stock[s]))
            #print(type(stock[s]))
            if type(stock[s]) == datetime.datetime:
                date = timestring.Date(str(stock[s])).date
                date = datetime.datetime.strftime(date,'%m-%d-%y')
                stock[s] = date
        firebase_db.child('Stocks').child(stock['id']).set(stock)
    #firebase_db.child('Stocks').set(json.dumps(stocks.values()))
    return render(request,"stocks/stocks_list.html", {'Stocks': stocks,'form_A':form_A,'form_B':form_B})

def AddStock(request):
    if request.method == "POST":
        form_A = forms.AddNewStock(request.POST)
        form_B = forms.goForIT(request.POST)
        if form_A.is_valid():
            form_A.save()
            return redirect('stocks:stocks')
    else:
        form_A = forms.AddNewStock()
        print('running in addstocks')
        form_B = forms.goForIT()

    stocks = Stock.objects.all().order_by('stock_name')
    return render(request,"stocks/stock_create.html",{'Stocks': stocks,'form_A':form_A,'form_B':form_B })

def get_LeData(request,*args,**kwargs):
    '''print(request.GET.keys())
    for key in request.GET.keys():
        print (str(key), request.GET.get(str(key)))'''

    '''data = {
        "val1": 100,
        "val2": 200,
    }'''
    chart_labels = []
    chart_points = []
    data_points = {"points":[]}
    try:
        stock_symbol_A = request.GET.get('symbol')
        print("This is the stock: " + str(stock_symbol_A))
        if stock_symbol_A != None:
            data = grab_stock_points(stock_symbol_A)
        else:
            if request.GET.get('search_stock_symbol') != None:
                stock_symbol_A = request.GET.get('search_stock_symbol')
                data = grab_stock_points(stock_symbol_A)
            else:
                data = grab_stock_points('INTL')
    except Exception:
        if request.GET.get('search_stock_symbol') != None:
            data = grab_stock_points(stock_symbol_A)
        else:
            data = grab_stock_points('INTL')
    print("This is the stock: " + str(stock_symbol_A))
    for s in data:
        data_point = {"date":str(s), "value":str(data[s]["SMA"])}

        #date = datetime.datetime.strptime(str(s),'%y%m%d')
        date = timestring.Date(str(s)).date
        date = datetime.datetime.strftime(date,'%m-%d-%y')
        chart_labels.append(str(date))
        chart_points.append(str(data[s]["SMA"]))
        data_points["points"].append(data_point)
    data_points = {
    "stock_name":request.GET.get('search_stock_symbol'),
    "dates":chart_labels[::-1],
    "values":chart_points[::-1],
    }

    return JsonResponse(data_points)
    #return JsonResponse(data)
