"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
# Blueprint('api',)
api = Blueprint('api', __name__)
# localhost:3001/
# locahost:3001/api/endpoint


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hola mundo desde react-flask-hello"
    }

    return jsonify(response_body), 200


@api.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data.get('email', None)
    password = data.get('password', None)
    # NO PUEDES GUARDAR EL PASSWORD LITERAL!!!!

    # Encriptarlo
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password, is_active=True)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify("Nuevo usuario creado con exito"), 201

    except Exception as error:
        db.session.rollback()
        return jsonify({"error": error}), 500


@api.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email_data = data.get("email", None)
    password = data.get("password", None)

    # Que exista un usuario con el email que nos dan
    user = User.query.filter_by(email=email_data).first()
    if not user:
        return jsonify({"error": "user not found"}), 404

    # Que la contraseña haga match
    passwords_match = check_password_hash(user.password, password)
    if not passwords_match:
        return jsonify({"error": "Password incorrecta"}), 401

    # Creamos nuestro token de acceso
    token_object = {"id": user.id, "email": user.email}
    token = create_access_token(token_object)
    return jsonify({"token": token}), 200


@api.route("/private", methods=["GET"])
@jwt_required()  # Decorador de jwt
def get_private_data():
    user = get_jwt_identity()
    return jsonify({"data": user}), 200
