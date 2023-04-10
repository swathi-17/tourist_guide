# # from datetime import datetime
from flaskapp import db, login_manager
from flaskapp import db
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Restaurant_name = db.Column(db.String(50))
    Cuisines = db.Column(db.String(100))
    Pricing_for_2 = db.Column(db.Integer)
    Locality = db.Column(db.String(100))
    Dining_Rating = db.Column(db.Float)
    Website = db.Column(db.String(100))
    Address = db.Column(db.String(100))
    Phone_No = db.Column(db.Integer)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    Timing = db.Column(db.String(50))
    Highlights = db.Column(ARRAY(db.String), nullable=True)
    Votes = db.Column(db.Float)
    Delivery = db.Column(db.Float)
    Takeaway = db.Column(db.Float)

    def __repr__(self):
        return f"Restaurant('{self.Restaurant_name}', '{self.Locality}')"

class Hotel():
    hotel_id = db.Column(db.Integer, primary_key=True)
    property_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    area = db.Column(db.String(50))
    city = db.Column(db.String(50))
    hotel_description = db.Column(db.String(500))
    hotel_facilities = db.Column(db.String(500))
    hotel_star_rating = db.Column(db.Float)
    image_urls = db.Column(db.String(500))
    locality = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    pageurl = db.Column(db.String(100))
    property_type = db.Column(db.String(20))
    province = db.Column(db.String(50))
    room_count = db.Column(db.Float)
    room_facilities = db.Column(db.String(100))
    room_type = db.Column(db.String(50))
    state = db.Column(db.String(50))
    rating = db.Column(db.Float)

    def __repr__(self):
        return f"Hotel('{self.property_name}', '{self.city}')"

class Attraction():
    attraction_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    description = db.Column(db.String(500))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    price = db.Column(db.Float)
    state = db.Column(db.String(50))
    street = db.Column(db.String(50))
    title = db.Column(db.String(50))
    totalScore = db.Column(db.Float)
    categories = db.Column(db.String(50))
    image_url = db.Column(db.String(500))

    def __repr__(self):
        return f"Hotel('{self.title}', '{self.city}')"

