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
http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"
proxies = {
	"https" : "http://proxy-us.intel.com:911"
}

response = requests.get(API_URL, params=data,proxies=proxies) 
for r in response:
	print(r)