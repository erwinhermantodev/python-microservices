import tornado.web
import requests

class ListingsHandler(tornado.web.RequestHandler):
    def get(self):
        # Forward GET request to listing service
        page_num = int(self.get_argument("page_num", default=1))
        page_size = int(self.get_argument("page_size", default=10))
        user_id = self.get_argument("user_id", default=None)
        url = f"http://localhost:6002/listings?page_num={page_num}&page_size={page_size}&user_id={user_id}"
        response = requests.get(url)
        
        if response.status_code == 200:
            listings = response.json()['listings']
            # Fetch user details for each listing
            for listing in listings:
                user_id = listing.pop('user_id')  # Remove user_id from listing
                user_url = f"http://localhost:6001/users/{user_id}"
                user_response = requests.get(user_url)
                if user_response.status_code == 200:
                    user = user_response.json()['user']
                    listing['user'] = user
                else:
                    listing['user'] = None
            # Return the modified response
            self.write({"result": True, "listings": listings})
        else:
            self.set_status(response.status_code)
            self.write({"result": False, "message": "Failed to retrieve listings"})

    def post(self):
        # Forward POST request to listing service
        user_id = self.get_argument("user_id")
        price = self.get_argument("price")
        listing_type = self.get_argument("listing_type")
        url = "http://localhost:6002/listings"
        payload = {"user_id": user_id, "price": price, "listing_type": listing_type}
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            self.write(response.json())
        else:
            self.set_status(response.status_code)
            self.write({"result": False, "message": "Failed to create listing"})
