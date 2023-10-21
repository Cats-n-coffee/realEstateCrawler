import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()
db_connection = os.environ["DB_CONNECTION"]

def read_listing_by_mls(cursor, mls_number):
    try:
        cursor.execute(
            "SELECT MlsNumber,StreetAddress,City,ZipCode FROM Listings WHERE [MlsNumber] = ?",
            (mls_number)
        )
        row = cursor.fetchone()

        return row
    except Exception as e:
        print(f"EXCEPTION READ {e}")

def update_listing(cursor, price, mls_number):
    try:
        cursor.execute(
            "UPDATE Listings SET Price=? WHERE MlsNumber=?",
            (price, mls_number)
        )
        cursor.commit()

    except Exception as e:
        print(f"EXCEPTION UPDATE {e}")

def insert_listing(cursor, listing):
    try:
       cursor.execute(
            "INSERT INTO Listings"
            "(MlsNumber, StreetAddress, City, ZipCode, Price, Beds, Baths, Sqft,"
            "Link, Site)"
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (listing['mls_number'], listing['street_address'], listing['city'], listing['zip'],
            listing['price'], listing['beds'], listing['baths'], listing['sqft'],
            listing['link'], listing['site'])
        )
       cursor.commit()

    except Exception as e:
        print(f"EXCEPTION INSERT {e}")

def make_connection():
    connection = pyodbc.connect(db_connection)
    cursor = connection.cursor()

    return connection, cursor

def store_listings(data):
    connection, cursor = make_connection();

    for listing in data:
        # read the listing by mlsnumber
        result = read_listing_by_mls(cursor, listing["mls_number"])
        db_lookup = False if result == None else True
        
        if db_lookup: # if exists update
            update_listing(cursor, listing["price"], listing["mls_number"])
        else:
            insert_listing(cursor, listing)

    connection.close()

    if os.path.exists("listingResults/remaxListings.json"):
        os.remove("listingResults/remaxListings.json")