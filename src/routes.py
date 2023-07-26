from flask import Flask, request, jsonify, Blueprint
from models import db, User, Characters, Planets, Starships, Favorites
from utils import APIException

api = Blueprint('api', __name__)

@api.route('/test', methods=['GET'])
def testAPI():
    return jsonify('YOUR API WORKS, CONGRATS'), 200

@api.route('/user', methods=['GET'])
def handle_USER():
    all_users = User.query.all()
    user_serialized = [user_name.serialize() for user_name in all_users]
    return jsonify(user_serialized), 200

@api.route('/planet', methods=['GET'])
def handle_PLANETS():
    all_planets = Planets.query.all()
    planet_serialized = [planet_name.serialize() for planet_name in all_planets]
    return jsonify(planet_serialized), 200

@api.route('/starship', methods=['GET'])
def handle_STARSHIPS():
    all_starships = Starships.query.all()
    starships_serialized = [starship_name.serialize() for starship_name in all_starships]
    return jsonify(starships_serialized), 200

@api.route('/character', methods=['GET'])
def handle_CHARACTERS():
    all_characters = Characters.query.all()
    character_serialized = [character_name.serialize() for character_name in all_characters]
    return jsonify(character_serialized), 200

@api.route('/planet', methods=['POST'])
def add_PLANETS():
    body = request.get_json() 
    planet_list = Planets(name=body['name'], gravity=body['gravity'], population=body['population'], climate=body['climate'])
    db.session.add(planet_list)
    db.session.commit()
    return 'PLANET CREATED SUCCESSFULLY', 200

@api.route('/starship', methods=['POST'])
def add_STARSHIPS():
    body = request.get_json() 
    starship_list = Starships(name=body['name'], model=body['model'], length=body['length'], pilots=body['pilots'])
    db.session.add(starship_list)
    db.session.commit()
    return 'STARSHIP CREATED SUCCESSFULLY', 200

@api.route('/character', methods=['POST'])
def add_CHARACTERS():
    body = request.get_json() 
    character_list = Characters(name=body['name'], height=body['height'], mass=body['mass'], home=body['home'])
    db.session.add(character_list)
    db.session.commit()
    return 'CHARACTER CREATED SUCCESSFULLY', 200


@api.route('/planet/<int:id>', methods=['DELETE'])
def delete_PLANETS(id):
    planet = Planets.query.get_or_404(id)
    db.session.delete(planet)
    db.session.commit()
    return 'PLANET DELETED SUCCESSFULLY', 200

@api.route('/starship/<int:id>', methods=['DELETE'])
def delete_STARSHIPS(id):
    starship = Starships.query.get_or_404(id)
    db.session.delete(starship)
    db.session.commit()
    return 'STARSHIP DELETED SUCCESSFULLY', 200

@api.route('/character/<int:id>', methods=['DELETE'])
def delete_CHARACTER(id):
    character = Characters.query.get_or_404(id)
    db.session.delete(character)
    db.session.commit()
    return 'CHARACTER DELETED SUCCESSFULLY', 200

@api.route('/users/favorites/<int:user_id>', methods=['GET'])
def get_user_favorites(user_id):
    favorites = Favorites.query.filter_by(user_id=user_id).all()
    serialized_favorites = [favorite.serialize() for favorite in favorites]
    return jsonify(favorites=serialized_favorites)

@api.route('/users/favorites', methods=['POST'])
def add_favorite():
    data = request.get_json()
    favorite = Favorites(
        user_id=data['user_id'],
        favorite_id=data['favorite_id'],
        favorite_type=data['favorite_type']
    )
    db.session.add(favorite)
    db.session.commit()
    return 'FAVORITE ADDED SUCCESSFULLY', 200

@api.route('/users/favorites/<int:favorite_id>', methods=['DELETE'])
def delete_favorite(favorite_id):
    favorite = Favorites.query.get(favorite_id)
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return 'FAVORITE DELETED SUCCESSFULLY', 200
    return 'Favorite not found.', 404

if __name__ == '__main__':
    api.run()