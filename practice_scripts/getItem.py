#Practice script - the getItem function basically queries the DPLA API for a
#specific item, and then returns some basic metadata from that item.

import random
from dpla.api import DPLA
from credentials import *

def getItem(dplaId):
    #create DPLA object using dpla module and API key
    dpla = DPLA(DPLA_KEY)

    #fetch item by id
    result = dpla.fetch_by_id([dplaId])

    title = result.items[0]["sourceResource"]["title"]
    dataProvider = result.items[0]["dataProvider"]

#    print(title)
#    return str(title)
    getItem.title = str(title)
    getItem.dataProvider = str(dataProvider)
