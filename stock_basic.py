################################################################################
####remember to include the "s" in the url so the proxy works effectively.
####REMEMBER TO INSTALL the alpha_vantage library for this code.
####alpha_vantage is a library we've found that's free and collects stock data.
################################################################################

def reverse_array(my_array):
        tmp_array = []
        for val in reversed(my_array):
                tmp_array.append(val)
        return tmp_array



import requests#, alpha_vantage
import json
import matplotlib.pyplot as plt

API_URL = "https://www.alphavantage.co/query"

data = {
	"function": "SMA",
	"time_period": 2,
	"series_type": "open",
	"symbol": "MSFT",
	"interval": "weekly",
	"apikey": "ksjendcksnfk",
}

proxies = {"https" : "http://proxy-us.intel.com:911"}

response = requests.get(API_URL, params=data,proxies=proxies) 
#for r in response:
#       print(str(r).replace("\n","")+'\n')

json_data = json.loads(response.text)

stock_key = 'Technical Analysis: SMA'

stock_sma = json_data[stock_key]
stock_dates = stock_sma.keys()

date_arry = []
stock_val = []


for sd in stock_dates:
        #print(sd,", ",stock_sma[sd]['SMA'])
        date_arry.append(sd)
        stock_val.append(float(stock_sma[sd]['SMA']))

#date_arry = reversed(date_arry)
#stock_val = reversed(stock_val)

plt.plot(reverse_array(stock_val))
plt.ylabel("Stock Values")
plt.show()


