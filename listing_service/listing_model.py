from peewee import Model, CharField, IntegerField, DateTimeField, SqliteDatabase
from datetime import datetime

db = SqliteDatabase('listings.db')

class BaseModel(Model):
    class Meta:
        database = db

class Listing(BaseModel):
    user_id = IntegerField()
    price = IntegerField()
    listing_type = CharField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "price": self.price,
            "listing_type": self.listing_type,
            "created_at": int(self.created_at.timestamp()),
            "updated_at": int(self.updated_at.timestamp())
        }
