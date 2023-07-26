from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(25), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    email = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f'<Character {self.email}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    height = db.Column(db.String(20), unique=True, nullable=False)
    mass = db.Column(db.String(20), unique=True, nullable=False)
    home = db.Column(db.String(20), unique=False, nullable=False)


    def __repr__(self):
        return f'<Characters {self.name}>'


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "home": self.home
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    gravity = db.Column(db.String(25), nullable=False)
    population = db.Column(db.String(25))
    climate = db.Column(db.String(25))

    def __repr__(self):
        return f'<Planets {self.name}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate
        }
    

class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    length = db.Column(db.Numeric(25,0))
    pilots = db.Column(db.String(50))

    def __repr__(self):
        return f'<Starships {self.name}'
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "length": self.length,
            "pilots": self.pilots
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    favorite_id = db.Column(db.Integer, unique=False)
    favorite_type = db.Column(db.String(100), unique=False)

    def __repr__(self):
        return f'<Favorite {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "favorite_id": self.favorite_id,
            "favorite_type": self.favorite_type
            # do not serialize the password, it's a security breach
        }