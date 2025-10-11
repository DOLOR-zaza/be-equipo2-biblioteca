from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.auth import User

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
def register_user():
    """
    Registra un nuevo usuario del sistema.
    """
    data = request.json
    user = User(username=data["username"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login_user():
    """
    Autentica a un usuario existente.
    """
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.password == data["password"]:
        return jsonify({"message": "Login successful"})
    return jsonify({"error": "Invalid credentials"}), 401
