from flask import Flask, make_response, jsonify
from flask_cors import CORS
from src.routes import auth, register
from src.config import APP, DB

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
                   "origins": [APP.CORS, "*"]
               }
            }, supports_credentials=True)

            # Registro de rutas
            cls.__register_routes()

        except Exception as e:
            return make_response(jsonify({
                "response": "Error iniciando server.",
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
