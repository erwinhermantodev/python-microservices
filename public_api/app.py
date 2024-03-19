import tornado.ioloop
import tornado.web
from listing_handler import ListingsHandler
from user_handler import UsersHandler

def make_app():
    return tornado.web.Application([
        (r"/public-api/listings", ListingsHandler),
        (r"/public-api/users", UsersHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(6000)
    print("Public API service is running. Listening on port 6000...")
    tornado.ioloop.IOLoop.current().start()
