from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.appointment import Appointment

appointment_bp = Blueprint("appointment_bp", __name__)

@appointment_bp.route("/", methods=["GET"])
def list_appointments():
    """
    Devuelve todas las citas médicas registradas.
    """
    appointments = Appointment.query.all()
    return jsonify([a.to_dict() for a in appointments])

@appointment_bp.route("/", methods=["POST"])
def create_appointment():
    """
    Crea una nueva cita médica.
    """
    data = request.json
    new_appointment = Appointment(
        patient_id=data["patient_id"],
        doctor_id=data["doctor_id"],
        date=data["date"],
        reason=data.get("reason", "")
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"message": "Appointment created successfully"}), 201
