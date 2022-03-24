from flask import Flask
from flask import make_response, jsonify
from flask_cors import CORS
from src.routes.auth_routes import auth
from src.routes.register_routes import register
from src.config.db_config import DB

class Aplication:
    @classmethod
    def create_app(cls):
        cls.app = Flask(__name__)
        cls.__configure()
        return cls.app

    @classmethod
    def __configure(cls):
        try:
            # Configuración de la base de datos
            cls.app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{DB.USER}:{DB.PASS}@{DB.HOST}:{DB.PORT}/{DB.NAME}'
            cls.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

            # Configuración de CORS
            CORS(cls.app, resources={
               r"/*": {
                   "origins": ["http://localhost:4200", "*"]
               }
            }, supports_credentials=True)

            # Registro de rutas
            cls.__register_routes()

        except Exception as e:
            return make_response(jsonify({
                "response": "Error starting server",
                "error": str(e)
            }), 500)

    @classmethod
    def __register_routes(cls):
        # Rutas de login
        cls.app.add_url_rule(auth["login"], view_func=auth["login_controller"])

        # Rutas de registro
        cls.app.add_url_rule(register["paciente"], view_func=register["paciente_controller"])
        cls.app.add_url_rule(register["medico"], view_func=register["medico_controller"])
        cls.app.add_url_rule(register["empleado"], view_func=register["empleado_controller"])
