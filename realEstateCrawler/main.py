from remaxCom import crawl_remax_com
from helpers.cleanData import clean_data_from_json
from db.dbOperations import main

if __name__ == "__main__":
    # crawl_remax_com()
    data = clean_data_from_json("listingResults/remaxListings.json")
    main(data)