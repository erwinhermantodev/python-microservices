import tornado.web
import requests

class UsersHandler(tornado.web.RequestHandler):
    def get(self):
        # Forward GET request to user service
        page_num = int(self.get_argument("page_num", default=1))
        page_size = int(self.get_argument("page_size", default=10))
        url = f"http://localhost:6001/users?page_num={page_num}&page_size={page_size}"
        response = requests.get(url)
        
        if response.status_code == 200:
            self.write(response.json())
        else:
            self.set_status(response.status_code)
            self.write({"result": False, "message": "Failed to retrieve users"})

    def post(self):
        # Forward POST request to user service
        name = self.get_argument("name")
        url = "http://localhost:6001/users"
        payload = {"name": name}
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            self.write(response.json())
        else:
            self.set_status(response.status_code)
            self.write({"result": False, "message": "Failed to create user"})
