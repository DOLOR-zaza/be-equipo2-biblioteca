from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.patient import Patient

patient_bp = Blueprint("patient_bp", __name__)

@patient_bp.route("/", methods=["GET"])
def list_patients():
    """
    Devuelve la lista de pacientes registrados.
    """
    patients = Patient.query.all()
    return jsonify([p.to_dict() for p in patients])

@patient_bp.route("/", methods=["POST"])
def create_patient():
    """
    Registra un nuevo paciente.
    """
    data = request.json
    new_patient = Patient(
        name=data["name"],
        age=data["age"],
        phone=data.get("phone")
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient added successfully"}), 201
