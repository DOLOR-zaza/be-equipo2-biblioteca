import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Configuración general de la aplicación Flask.
    """
    SECRET_KEY = os.getenv("SECRET_KEY", "bibiano123")
    JSON_SORT_KEYS = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'consultorio.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
