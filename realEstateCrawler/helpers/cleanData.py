import json

def clean_data_from_json(file: str):
    json_to_dictionary = None

    with open(file, 'r') as f:
        json_to_dictionary = json.load(f)

    cleanListings = []
    for listing in json_to_dictionary:
        updatedListing = {}
        splitURL = listing["address"].split("/")

        updatedListing["mls_number"] = splitURL[-1]
        updatedListing["street_address"] = splitURL[6]
        updatedListing["city"] = splitURL[4]
        updatedListing["zip"] = splitURL[6][-5:]
        updatedListing["price"] = listing["price"].strip()
        updatedListing["beds"] = int(listing["Beds"])
        updatedListing["baths"] = int(listing["Baths"])
        updatedListing["sqft"] = int("".join(listing["Sq Ft"].split(",")))
        updatedListing["link"] = listing["address"]
        updatedListing["site"] = splitURL[2]

        cleanListings.append(updatedListing)

    return cleanListings