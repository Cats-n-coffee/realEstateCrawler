import json
# from datetime import datetime

def convert_to_json_file(data):
    # dateObj = int(datetime.now().timestamp())
    with open("listingResults/remaxListings.json", "w") as file:
        file.write(json.dumps(data))
