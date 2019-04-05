"""Google API Demo for PyStockAnalyze

Grabs some articles related to a stock being analyzed
"""

__author__ = 'Lennard Streat'

import pprint
from googleapiclient.discovery import build
import httplib2, requests, json

from build import projenv

# Commenting before this function--the function works properly now
# But the user must create a projenv.py file in the build folder
def cse_standard():
	cse_query_str = "INTC"

	proxy_info = httplib2.ProxyInfo(proxy_type=httplib2.socks.PROXY_TYPE_HTTP,
		proxy_host=projenv.glob_proxy_host,
		proxy_port=projenv.glob_proxy_port)

	httpreq = httplib2.Http(proxy_info = proxy_info)

	service = build(serviceName='customsearch',
		version='v1',
		developerKey=projenv.cse_api_key,
		http=httpreq)

	resp = service.cse().list(
		q=cse_query_str,
		cx=projenv.cse_eng_id,
		).execute()

	pprint.pprint(resp)


if __name__ == '__main__':
	cse_standard()