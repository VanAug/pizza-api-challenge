# server/controllers/restaurant_pizza_controller.py
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from server.models.restaurant_pizza import Restaurant_Pizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models import db

restaurant_pizza_bp = Blueprint("restaurant_pizzas", __name__)

#Post a new pizza-restaurant relationship
@restaurant_pizza_bp.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['price', 'pizza_id', 'restaurant_id']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({"errors": [f"Missing required fields: {', '.join(missing_fields)}"]}), 400
    
    # Extract values
    price = data['price']
    pizza_id = data['pizza_id']
    restaurant_id = data['restaurant_id']
    
    # Validate price type and range
    try:
        price = float(price)
        if not (1 <= price <= 30):
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    except (TypeError, ValueError):
        return jsonify({"errors": ["Invalid price format. Must be a number"]}), 400
    
    # Check if pizza exists
    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        return jsonify({"errors": [f"Pizza with ID {pizza_id} not found"]}), 404
    
    # Check if restaurant exists
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({"errors": [f"Restaurant with ID {restaurant_id} not found"]}), 404
    
    # Create new relationship
    rp = Restaurant_Pizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    
    # Commit with error handling
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"errors": ["Database integrity error. Possible duplicate entry."]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [f"Server error: {str(e)}"]}), 500

    # Return successful response
    return jsonify({
        "id": rp.id,
        "price": rp.price,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }), 201