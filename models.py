import os
from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env
MONGO_URI=os.environ["MONGO_URI"]    
connect('marketPlaceDB', host=MONGO_URI)

class Seller(Document):
    seller_name = StringField(required=True, max_length=50)
    seller_city = StringField(required=True)
    seller_email = EmailField(required=True)
    seller_phone = StringField(required=True)
    seller_listings = ListField(StringField(), default=[])
    password_hash = StringField()
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        is_valid = check_password_hash(self.password_hash, password)
        return is_valid

class Category(Document):
    name = StringField(required=True)

class ProductListing(Document):
    category_id = ReferenceField(Category)
    product_name = StringField(required=True, max_length=50)
    product_price = StringField(required=True)
    product_description = StringField()
    seller_id = ReferenceField(Seller)

    meta = {'indexes': [
        {'fields': ['$product_name', "$product_description"],
         'default_language': 'english',
        }
    ]}

    @property
    def serialize(self):
        return {
            "product_name": self.product_name,
            "product_description": self.product_description,
            "product_price": self.product_price
        }


