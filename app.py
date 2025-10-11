from flask import Flask
from src.config import Config
from src.extensions import db, migrate
from src.api import register_blueprints


def create_app():
    """
    Crea y configura una instancia de la aplicación Flask usando
    el patrón Application Factory.

    Esta función inicializa:
    - Configuración de la app (SECRET_KEY, DB, etc.)
    - Extensiones (SQLAlchemy, Migrate)
    - Blueprints para las rutas de la API

    Returns:
        Flask: instancia configurada de la aplicación
    """
    app = Flask(__name__)

    # Cargar configuración desde el archivo src/config.py
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar los blueprints de la API
    register_blueprints(app)

    # Ruta de prueba para confirmar que la app funciona
    @app.route('/')
    def index():
        return {
            "message": "API del Consultorio Médico activa",
            "status": "ok"
        }

    return app


# Punto de entrada principal
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
