import random
from dpla.api import DPLA
from credentials import DPLA_KEY

def findItem(dplaId, hub):
    # Create DPLA object using dpla module and API key
    # API key comes from credentials.py file
    dpla = DPLA(DPLA_KEY)

    try:
        sourceItem = dpla.fetch_by_id([dplaId])

        print(sourceItem.items[0]["sourceResource"]["title"])

        if "subject" in sourceItem.items[0]["sourceResource"]:
            # Create new object containing all of the subjects from fetched item
            subjects = sourceItem.items[0]["sourceResource"]["subject"]

            # Print number of subject terms
            #print(len(subjects))

            # Get random integer within the number of subjects in record
            randA = random.randint(0, (len(subjects)-1))
            #print(randA)

            # Use random integer to get subject term corresponding to it
            # Replace " - " with " " to deal with an issue when searching DPLA
            findItem.randomSubject = subjects[randA]["name"].replace(" - ", " ")
            print("Searching for \'" + findItem.randomSubject + "\'...")

            # Query DPLA API for items matching the random subject selected
            fields = {"provider": hub}
            findItem.result1 = dpla.search(findItem.randomSubject, searchFields=fields, page_size=60)

            print("Results found: " + str(findItem.result1.count))

            # Select four random items from the results returned from DPLA
            try:
                findItem.resultDisplay = random.sample(findItem.result1.items, 4)
            # If there are less than 4 results, just copy them all
            except ValueError:
                findItem.resultDisplay = findItem.result1.items

        # Error handling for items that don't have subjects
        else:
            findItem.randomSubject = "No subjects found in this item. Try another!"
            findItem.result1 = "[]"
            findItem.resultDisplay = ""

            print(findItem.randomSubject)

    #    if result2.count == 0:
    #    	print("Sorry, no results found for \'"+random_subject+"\'.  Try again!")

    #    else:
    #    	for item in result2.items:
    #    		title = item["sourceResource"]["title"]
    #    		identifier = item["@id"]
    #    		dataProvider = item["dataProvider"]
    #    		subjects = item["sourceResource"]["subject"]

    #    		print("**SIMILAR ITEM**")
    #    		print(title)
    #    		print(identifier)
    #    		print(dataProvider)
    #    		print(subjects)

    # Error handling for input that doesn't return a DPLA record (e.g. isn't a DPLA id)
    except AttributeError:
        findItem.randomSubject = "Woops, that doesn't look like a DPLA ID.  Try again!"
        findItem.result1 = "[]"
        findItem.resultDisplay = ""

        print(findItem.randomSubject)
