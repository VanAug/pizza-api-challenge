# server/seed.py
from server.app import app
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import Restaurant_Pizza

# Sample pizza data with realistic ingredients
pizza_data = [
    {"name": "Margherita", "ingredients": "Tomato sauce, Mozzarella, Basil"},
    {"name": "Pepperoni", "ingredients": "Tomato sauce, Mozzarella, Pepperoni"},
    {"name": "Vegetarian", "ingredients": "Tomato sauce, Mozzarella, Bell peppers, Mushrooms, Olives"},
    {"name": "Hawaiian", "ingredients": "Tomato sauce, Mozzarella, Ham, Pineapple"},
    {"name": "Supreme", "ingredients": "Tomato sauce, Mozzarella, Pepperoni, Sausage, Onions, Bell peppers"},
    {"name": "BBQ Chicken", "ingredients": "BBQ sauce, Mozzarella, Grilled chicken, Red onions, Cilantro"},
    {"name": "Mushroom Truffle", "ingredients": "Cream sauce, Mozzarella, Mushrooms, Truffle oil, Parmesan"},
    {"name": "Four Cheese", "ingredients": "Tomato sauce, Mozzarella, Gorgonzola, Parmesan, Ricotta"},
    {"name": "Buffalo Chicken", "ingredients": "Buffalo sauce, Mozzarella, Chicken, Red onions, Ranch drizzle"},
    {"name": "Mediterranean", "ingredients": "Olive oil, Feta, Spinach, Kalamata olives, Red onions, Artichokes"}
]

# Sample restaurant data with realistic names
restaurant_data = [
    {"name": "Slice of Heaven", "address": "123 Main St, New York"},
    {"name": "Crust & Craft", "address": "456 Oak Ave, Brooklyn"},
    {"name": "Pizza Paradiso", "address": "789 Pine Rd, Queens"},
    {"name": "The Doughminator", "address": "101 Maple Blvd, Bronx"},
    {"name": "Cheesy Does It", "address": "202 Elm St, Staten Island"},
    {"name": "Fire & Flour", "address": "303 Cedar Ln, Jersey City"},
    {"name": "Mamma Mia's", "address": "404 Birch Dr, Hoboken"},
    {"name": "Pizzalicious", "address": "505 Spruce Ave, Newark"},
    {"name": "The Golden Crust", "address": "606 Willow Way, Yonkers"},
    {"name": "Brick Oven Bliss", "address": "707 Chestnut Ct, White Plains"}
]

def seed_database():
    with app.app_context():
        # Clear existing data in safe order
        Restaurant_Pizza.query.delete()
        Pizza.query.delete()
        Restaurant.query.delete()
        db.session.commit()

        # Create restaurants
        restaurants = []
        for data in restaurant_data:
            restaurant = Restaurant(name=data["name"], address=data["address"])
            restaurants.append(restaurant)
            db.session.add(restaurant)
        
        db.session.commit()
        print(f"✅ Seeded {len(restaurants)} Restaurants")

        # Create pizzas
        pizzas = []
        for data in pizza_data:
            pizza = Pizza(name=data["name"], ingredients=data["ingredients"])
            pizzas.append(pizza)
            db.session.add(pizza)
        
        db.session.commit()
        print(f"✅ Seeded {len(pizzas)} Pizzas")

        # Create restaurant-pizza relationships
        restaurant_pizzas = []
        
        # Assign each restaurant 2-4 random pizzas
        for restaurant in restaurants:
            num_pizzas = 2 + restaurant.id % 3  # Vary between 2-4 pizzas
            
            for i in range(num_pizzas):
                pizza_idx = (restaurant.id + i) % len(pizzas)  # Wrap around
                price = 9.99 + (restaurant.id + pizza_idx) % 10  # $10-20 range
                
                rp = Restaurant_Pizza(
                    price=round(price, 2),
                    pizza_id=pizzas[pizza_idx].id,
                    restaurant_id=restaurant.id
                )
                restaurant_pizzas.append(rp)
                db.session.add(rp)
        
        db.session.commit()
        print(f"✅ Seeded {len(restaurant_pizzas)} Restaurant-Pizza Relationships")
        
        # Special relationships to demonstrate many-to-many
        # 1. One pizza available in multiple restaurants
        margherita = next(p for p in pizzas if p.name == "Margherita")
        for i in range(3):
            rp = Restaurant_Pizza(
                price=12.50,
                pizza_id=margherita.id,
                restaurant_id=restaurants[i].id
            )
            db.session.add(rp)
        
        # 2. One restaurant with multiple pizzas
        crust_craft = next(r for r in restaurants if r.name == "Crust & Craft")
        for pizza in pizzas[:4]:
            rp = Restaurant_Pizza(
                price=14.99,
                pizza_id=pizza.id,
                restaurant_id=crust_craft.id
            )
            db.session.add(rp)
        
        db.session.commit()
        print(f"✅ Added special relationship cases")
        
        print("🌱 Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()