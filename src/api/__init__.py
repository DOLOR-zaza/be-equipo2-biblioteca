from flask import Blueprint

# Importamos los blueprints de cada módulo
from .patient import patient_bp
from .doctor import doctor_bp
from .appointment import appointment_bp
from .auth import auth_bp


def register_blueprints(app):
    """Registra todos los blueprints del proyecto en la app Flask."""
    app.register_blueprint(patient_bp, url_prefix="/api/patients")
    app.register_blueprint(doctor_bp, url_prefix="/api/doctors")
    app.register_blueprint(appointment_bp, url_prefix="/api/appointments")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
