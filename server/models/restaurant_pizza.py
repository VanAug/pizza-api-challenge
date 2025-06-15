from server.models import db

class Restaurant_Pizza(db.Model):
    
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)