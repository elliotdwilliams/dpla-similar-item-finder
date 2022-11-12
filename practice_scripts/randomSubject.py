#Practice script - this script accepts a DPLA ID from user input, then queries
#the DPLA API to get that item record, extract a random subject, and then search
#DPLA for items with that subject in the Portal to Texas History.
#This script formed the basis for findItem.py.

import random
from dpla.api import DPLA
from credentials import *

#create DPLA object using dpla module and API key from credentials
dpla = DPLA(DPLA_KEY)

#get DPLA id from user input
dplaid = input("DPLA item ID: ")

result = dpla.fetch_by_id([dplaid])

print(result.items[0]["sourceResource"]["title"])

#create new object containing all of the subjects from fetched item
subjects = result.items[0]["sourceResource"]["subject"]

##print number of subject terms
#print(len(subjects))

#get random integer within the number of subjects in record
randA = random.randint(0,(len(subjects)-1))
#print(randA)

#use random integer to get subject term corresponding to it
random_subject = subjects[randA]["name"]
print("Searching for \'"+random_subject+"\'...")

#query DPLA API for items matching the random subject selected
fields = {"provider" : "Portal to Texas History"}
result2 = dpla.search(random_subject, searchFields=fields, page_size=3)

print("Results found: "+str(result2.count))

if result2.count == 0:
	print("Sorry, no results found for \'"+random_subject+"\'.  Try again!")

else:
	for item in result2.items:
		title = item["sourceResource"]["title"]
		identifier = item["@id"]
		dataProvider = item["dataProvider"]
		subjects = item["sourceResource"]["subject"]

		print("**SIMILAR ITEM**")
		print(title)
		print(identifier)
		print(dataProvider)
		print(subjects)
