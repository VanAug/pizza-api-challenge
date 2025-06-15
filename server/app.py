# server/app.py

from flask import Flask
from flask_migrate import Migrate
from server.config import Config
from server.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    with app.app_context():
        from server.models import pizza, restaurant, restaurant_pizza
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
