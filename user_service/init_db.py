from user_model import db, User

def initialize_database():
    db.connect()
    db.create_tables([User], safe=True)
