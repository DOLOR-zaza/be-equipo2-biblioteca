from src.extensions import db

class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    reason = db.Column(db.String(200))

    doctor = db.relationship("Doctor", backref="appointments")
    patient = db.relationship("Patient", backref="appointments")

    def to_dict(self):
        return {
            "id": self.id,
            "doctor": self.doctor.name,
            "patient": self.patient.name,
            "date": self.date,
            "reason": self.reason,
        }
