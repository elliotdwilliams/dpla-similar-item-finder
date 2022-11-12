#Practice script - this script just queries the DPLA API for a specific item,
#and then displays some basic metadata for that item.

import random
from dpla.api import DPLA
from credentials import *

#create DPLA object using dpla module and API key
dpla = DPLA(DPLA_KEY)

#get DPLA id from user input
dplaid = input("DPLA item ID: ")

result = dpla.fetch_by_id([dplaid])

print(result.items[0]["sourceResource"]["title"])

#create new object containing all of the subjects from fetched item
subjects = result.items[0]["sourceResource"]["subject"]

#print number of subject terms
print(len(subjects))

#parse subject object to list out all of subject values
for subject in subjects:
    subjectName = subject["name"]

    print(subjectName)
