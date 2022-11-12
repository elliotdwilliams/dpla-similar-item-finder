#Practice script - this script queries the DPLA API for all items from TDL, and
#uses randomly generated values to get a page of the results and an item within
#those results.  Then it extracts some data for that item and outputs it.

import random
from dpla.api import DPLA
from credentials import *

#create DPLA object using dpla module and API key
dpla = DPLA(DPLA_KEY)

#generate random number to use as page value
random_page = random.randint(0, 100)

#create results set of all DPLA items where provider is TDL
fields = {"provider" : "Texas Digital Library"}
result = dpla.search(searchFields=fields, page_size=100, page=random_page)

#get random item from the results
items = random.sample(result.items, 1)

#print title, identifier, and dataProvider of results from API call
for item in items:
	title = item["sourceResource"]["title"]
	identifier = item["@id"]
	dataProvider = item["dataProvider"]
#	subject = item["sourceResource"]["subject"]["name"]
	subjects = item["sourceResource"]["subject"]

	print(title)
	print(identifier)
	print(dataProvider)
	print(subjects)
