from server.models import db

class Restaurant(db.Model):

    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship('Restaurant_Pizza', back_populates='restaurant', cascade='all, delete')
