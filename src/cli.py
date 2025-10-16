from click import echo
from src.extensions import db
from src.models import Doctor, Patient, Appointment

def register_seed_command(app):
    @app.cli.command("seed")
    def seed():
        """Carga datos iniciales de ejemplo."""
        if Doctor.query.first():
            echo("Seed ya aplicado.")
            return

        doc = Doctor(name="Dr. López", specialty="Cardiología")
        pat = Patient(name="Ana Torres", email="ana@example.com")
        appo = Appointment(doctor=doc, patient=pat, date="2025-10-11", reason="Chequeo general")

        db.session.add_all([doc, pat, appo])
        db.session.commit()
        echo("Datos semilla cargados correctamente.")
