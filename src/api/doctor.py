from flask import Blueprint, jsonify, request
from src.extensions import db
from src.models import Doctor

bp = Blueprint("doctors", __name__)

@bp.get("/")
def list_doctors():
    """Devuelve todos los doctores registrados."""
    doctors = Doctor.query.all()
    return jsonify([d.to_dict() for d in doctors])

@bp.post("/")
def create_doctor():
    data = request.get_json()
    doctor = Doctor(name=data["name"], specialty=data["specialty"])
    db.session.add(doctor)
    db.session.commit()
    return jsonify(doctor.to_dict()), 201
