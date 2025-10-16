from src.api.appointment import bp as appointment_bp
from src.api.auth import bp as auth_bp
from src.api.doctor import bp as doctor_bp
from src.api.patient import bp as patient_bp


def register_blueprints(app):
    """Registra todos los blueprints del proyecto en la app Flask."""
    app.register_blueprint(patient_bp, url_prefix="/api/patients")
    app.register_blueprint(doctor_bp, url_prefix="/api/doctors")
    app.register_blueprint(appointment_bp, url_prefix="/api/appointments")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
