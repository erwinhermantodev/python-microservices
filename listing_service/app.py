import tornado.ioloop
import tornado.web
from listing_controller import ListingsController
from init_db import initialize_database

def make_app():
    initialize_database()
    return tornado.web.Application([
        (r"/listings", ListingsController),
        (r"/listings/(\d+)", ListingsController),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(6002)
    print("Listing service is running. Listening on port 6002...")
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\nListing service stopped.")
