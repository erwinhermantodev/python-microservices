from tornado.web import RequestHandler
from listing_model import Listing
import json

class ListingsController(RequestHandler):
    def get(self):
        page_num = int(self.get_argument("page_num", default=1))
        page_size = int(self.get_argument("page_size", default=10))
        listings = Listing.select().paginate(page_num, page_size)

        response = {
            "result": True,
            "listings": [listing.serialize() for listing in listings]
        }
        self.write(response)

    def post(self):
        user_id = int(self.get_argument("user_id"))
        price = int(self.get_argument("price"))
        listing_type = self.get_argument("listing_type")

        listing = Listing.create(user_id=user_id, price=price, listing_type=listing_type)

        response = {
            "result": True,
            "listing": listing.serialize()
        }
        self.write(response)
