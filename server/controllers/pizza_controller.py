
from flask import Blueprint, jsonify
from server.models.pizza import Pizza
from server.models import db

pizza_bp = Blueprint("pizzas", __name__)

#Get all pizzas
@pizza_bp.route("/pizzas", methods=["GET"])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "ingredients": p.ingredients
    } for p in pizzas])

#Get pizza by id
@pizza_bp.route("/pizzas/<int:id>", methods=["GET"])
def get_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({"error": "Pizza not found"}), 404

    return jsonify({
        "id": pizza.id,
        "name": pizza.name,
        "ingredints": pizza.ingredients,
        
    })

#Delete pizza by id
@pizza_bp.route("/pizzas/<int:id>", methods=["DELETE"])
def delete_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({"error": "Pizza not found"}), 404

    db.session.delete(pizza)
    db.session.commit()
    return "", 204
