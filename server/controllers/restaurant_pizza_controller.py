
from flask import Blueprint, request, jsonify
from server.models import Restaurant_Pizza, Pizza, Restaurant, db

restaurant_pizza_bp = Blueprint("restaurant_pizzas", __name__)

@restaurant_pizza_bp.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    rp = Restaurant_Pizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    return jsonify({
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza.id,
        "restaurant_id": rp.restaurant.id,
        "pizza": {
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        },
        "restaurant": {
            "id": rp.restaurant.id,
            "name": rp.restaurant.name,
            "address": rp.restaurant.address
        }
    }), 201
