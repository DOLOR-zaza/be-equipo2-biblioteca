from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.doctor import Doctor

doctor_bp = Blueprint("doctor_bp", __name__)

@doctor_bp.route("/", methods=["GET"])
def list_doctors():
    """
    Devuelve todos los doctores registrados en el sistema.
    """
    doctors = Doctor.query.all()
    return jsonify([d.to_dict() for d in doctors])

@doctor_bp.route("/", methods=["POST"])
def create_doctor():
    """
    Registra un nuevo doctor.
    """
    data = request.json
    new_doctor = Doctor(
        name=data["name"],
        specialty=data["specialty"]
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({"message": "Doctor added successfully"}), 201
