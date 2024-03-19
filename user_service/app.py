import tornado.ioloop
import tornado.web
from user_controller import UsersController
from init_db import initialize_database
import json
from datetime import datetime

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.timestamp() * 1000000 
        return super().default(obj)

def make_app():
    initialize_database()
    return tornado.web.Application([
        (r"/users", UsersController),
        (r"/users/(\d+)?", UsersController),
    ], json_encoder=CustomJsonEncoder) 

if __name__ == "__main__":
    app = make_app()
    app.listen(6001)
    print("User service is running. Listening on port 6001...")
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\nUser service stopped.") 
