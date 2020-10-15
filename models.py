import os
from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env
MONGO_URI=os.environ["MONGO_URI"]    
connect('marketPlaceDB', host=MONGO_URI)

class sellerMDB(Document):
    seller_name = StringField(required=True, max_length=50)
    seller_city = StringField(required=True)
    seller_email = EmailField(required=True)
    seller_city_phone = StringField(required=True)
    seller_listings = ListField(StringField(), default=[])
    password_hash = StringField()
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        is_valid = check_password_hash(self.password_hash, password)
        return is_valid

