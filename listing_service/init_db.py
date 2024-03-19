from listing_model import db, Listing

def initialize_database():
    db.connect()
    db.create_tables([Listing], safe=True)
