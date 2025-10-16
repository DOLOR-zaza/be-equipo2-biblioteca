from flask import Flask
from src.config import Config
from src.extensions import db, migrate
from src.api import register_blueprints
from src.cli import register_seed_command


def create_app():
    app = Flask(__name__)

    # Cargar configuración desde el archivo src/config.py
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar los blueprints de la API
    register_blueprints(app)

    # Registrar comandos CLI personalizados
    register_seed_command(app)

    # Ruta base de prueba
    @app.route('/')
    def index():
        return {
            "message": "API del Consultorio Médico activa",
            "status": "ok"
        }

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
