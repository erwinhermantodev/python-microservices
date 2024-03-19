import json
from datetime import datetime
from tornado.web import RequestHandler
from user_model import User

class UsersController(RequestHandler):
    def get(self, user_id=None):
        if user_id:
            user = User.get_or_none(User.id == user_id)
            if user:
                response = {
                    "result": True,
                    "user": user.serialize()
                }
            else:
                response = {
                    "result": False,
                    "message": "User not found"
                }
        else:
            page_num = int(self.get_argument("page_num", default=1))
            page_size = int(self.get_argument("page_size", default=10))
            users = User.select().paginate(page_num, page_size)

            response = {
                "result": True,
                "users": [user.serialize() for user in users]
            }
        self.write(response)

    def post(self):
        name = self.get_argument("name")
        user = User.create(name=name)

        response = {
            "result": True,
            "user": user.serialize()
        }
        self.write(response)
