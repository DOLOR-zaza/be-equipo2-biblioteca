import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = "bibiano1234"
    JSON_SORT_KEYS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'consultorio.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
