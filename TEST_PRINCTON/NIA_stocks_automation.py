################################################################################
####remember to include the "s" in the url so the proxy works effectively.
####REMEMBER TO INSTALL the alpha_vantage library for this code.
####alpha_vantage is a library we've found that's free and collects stock data.
################################################################################

import requests, alpha_vantage
 
API_URL = "https://www.alphavantage.co/query"

data = {
	"function": "SMA",
	"time_period": 10,
	"series_type": "open",
	"symbol": "MSFT",
	"interval": "weekly",
	"apikey": "ksjendcksnfk",
}

proxies = {
	"https" : "http://proxy-us.intel.com:911"
}

response = requests.get(API_URL, params=data,proxies=proxies) 
for r in response:
	print(str(r).replace("\n","")+'\n')