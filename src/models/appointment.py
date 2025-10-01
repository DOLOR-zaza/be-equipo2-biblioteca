from .patient import Patient
from .doctor import Doctor
from datetime import datetime

class Appointment:
    def __init__(self, id: int, patient: Patient, doctor: Doctor, date: datetime, status: str):
        self.id = id
        self.patient_id = patient.id   # toma el id del objeto Patient
        self.doctor_id = doctor.id     # toma el id del objeto Doctor
        self.date = date
        self.status = status
