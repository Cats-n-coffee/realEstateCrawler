import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()
db_connection = os.environ["DB_CONNECTION"]

def read_listing_by_mls(cursor, mls_number):
    print(f"Lisitng read {mls_number}")
    try:
        cursor.execute(
            "SELECT MlsNumber,StreetAddress,City,ZipCode FROM Listings WHERE [MlsNumber] = ?",
            (mls_number)
        )
        row = cursor.fetchall()
        
        if row is None:
            return False
        
        return row
    except Exception as e:
        print(f"EXCEPTION READ {e}")

def update_listing(cursor, mls_number):
    print('will update')

def insertListing(cursor, listing):
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
    except Exception as e:
        print(f"EXCEPTION INSERT {e}")

def make_connection():
    connection = pyodbc.connect(db_connection)
    cursor = connection.cursor()

    return cursor

def main(data):
    cursor = make_connection();

    for listing in data:
        # read the listing by mlsnumber
        db_lookup = False if read_listing_by_mls(cursor, listing['mls_number']) == None else True
        print(db_lookup)
        # if exists update
        if db_lookup:
            update_listing(cursor, listing['mls_number'])
        # else insert
    # insertListing(cursor, data[0])
    
    # cursor.execute("SELECT * FROM Listings")

    # for row in cursor:
    #     print('row = %r' % (row,))