from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from .restaurant import Restaurant
from .pizza import Pizza
from .restaurant_pizza import Restaurant_Pizza


metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
