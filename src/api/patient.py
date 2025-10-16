from flask import Blueprint, jsonify, request
from src.extensions import db
from src.models import Patient

patient_bp = Blueprint("patients", __name__)

@patient_bp.get("/")
def get_patients():
    return jsonify([p.to_dict() for p in Patient.query.all()])

@patient_bp.post("/")
def add_patient():
    data = request.get_json()
    new_patient = Patient(name=data["name"], email=data["email"], phone=data.get("phone"))
    db.session.add(new_patient)
    db.session.commit()
    return jsonify(new_patient.to_dict()), 201
