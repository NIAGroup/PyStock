################################################################################
####remember to include the "s" in the url so the proxy works effectively.
####REMEMBER TO INSTALL the alpha_vantage library for this code.
####alpha_vantage is a library we've found that's free and collects stock data.
################################################################################

import json, requests, alpha_vantage, openpyxl
import matplotlib.pyplot as plt
from openpyxl import Workbook
row = 1
col = 1
wb = Workbook()
ws = wb.create_sheet("Main")
data_array = []
array_corrected = []
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
try:
    response = requests.get(API_URL, params=data,proxies=proxies)
except Exception:
    response = requests.get(API_URL, params=data)
arr = response.text.split("{")

'''for l in arr:
    detes =  l.replace("{","")
    detes = detes.replace("\n","")
    print(detes)
    ws.cell(row,col,detes)
    row+=1'''
js = json.loads(response.text)
d = js["Technical Analysis: SMA"]
row = 1
col = 1

for s in d:
	if(row>1):
	    stringer_a = str(s)
	    stringer_b = str(d[s]["SMA"])
	    data_array.append(float(stringer_b))
	    print(stringer_a+"\t"+stringer_b)
	    ws.cell(row-1,col,stringer_a)
	    ws.cell(row-1,col+1,stringer_b)
	row+=1
wb.save("results.xlsx")
for x in range(len(data_array)-1,-1,-1):
	array_corrected.append(data_array[x])
plt.plot(array_corrected)
plt.show()
