from flask import Flask
from .config import Config
from .extensions import db, migrate
from .api.appointment import appointment_bp
from .api.auth import auth_bp
from .api.doctor import doctor_bp
from .api.patient import patient_bp

def create_app():
    """
    Crea y configura la instancia principal de la aplicación Flask.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints
    app.register_blueprint(appointment_bp, url_prefix="/api/appointments")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(doctor_bp, url_prefix="/api/doctors")
    app.register_blueprint(patient_bp, url_prefix="/api/patients")

    return app
