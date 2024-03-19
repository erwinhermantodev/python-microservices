from peewee import Model, CharField, DateTimeField, SqliteDatabase
from datetime import datetime

db = SqliteDatabase('users.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": int(self.created_at.timestamp()),
            "updated_at": int(self.updated_at.timestamp())
        }

