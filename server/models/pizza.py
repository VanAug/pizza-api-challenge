from server.models import db

class Pizza(db.Model):
    
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    ingredients = db.Column(db.String, nullable = False)

    restaurant_pizza = db.relationship("Restaurant_Pizza", back_populates = "pizzas")