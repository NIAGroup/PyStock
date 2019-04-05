"""Google API Demo for PyStockAnalyze

Grabs some articles related to a stock being analyzed
"""

__author__ = 'Lennard Streat'

import pprint
from googleapiclient.discovery import build

import httplib2
import json


def main():
	proxy_info = httplib2.ProxyInfo(proxy_type=httplib2.socks.PROXY_TYPE_HTTP,
		#proxy_host=xx.xx.xxx.xx,
		#proxy_port=xxxx)
	

	httpreq = httplib2.Http(proxy_info = proxy_info)
	
	resp, content = httpreq.request("http://www.google.com/", "GET")
	print(type(resp))
	print(type(content))
	print(resp.keys())
	print(resp["date"])
	#print(content.decode('ISO-8859-1'))

	#parsed = json.loads(content)

	"""
	service = build('customsearch', 'v1', developerKey="AIzaSyDRRpR3GS1F1_jKNNM9HCNd2wJQyPG3oN0")

	res = service.cse().list(
		q='lectures',
		cx='017576662512468239146:omuauf_lfve',
		).execute()
	"""

if __name__ == '__main__':
	main()