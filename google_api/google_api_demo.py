#!python
"""Google API Demo for PyStockAnalyze

Grabs some articles related to a stock being analyzed
"""

__author__ = 'Lennard Streat'

import pprint
from googleapiclient.discovery import build

def main():
	service = build('customsearch', 'v1', developerKey="AIzaSyDRRpR3GS1F1_jKNNM9HCNd2wJQyPG3oN0")

	res = service.cse().list(
		q='lectures',
		cx='017576662512468239146:omuauf_lfve',
		).execute()

if __name__ == '__main__':
	main()