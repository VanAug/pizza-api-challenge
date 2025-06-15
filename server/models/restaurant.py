from server.models import db

class Restaurant(db.Model):

    __tablename__ = "restaurants"
    
    passid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)