# server/app.py

from flask import Flask
from flask_migrate import Migrate
from server.config import Config
from server.models import db
from server.controllers import all_blueprints

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)

for bp in all_blueprints:
    app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(debug=True)
