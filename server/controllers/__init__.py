from .restaurant_controller import restaurant_bp
from .pizza_controller import pizza_bp
from .restaurant_pizza_controller import restaurant_pizza_bp

all_blueprints = [restaurant_bp, pizza_bp, restaurant_pizza_bp]