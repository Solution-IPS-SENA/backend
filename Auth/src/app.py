from flask import Flask
from flask import make_response, jsonify
from os import getenv
from flask_cors import CORS
from src.routes import *
from src.config.db_config import DB

class Aplication:
    @classmethod
    def create_app(cls):
        cls.app: Flask = Flask(__name__)
        cls.__configure()
        return cls.app

    @classmethod
    def __configure(cls):
        try:
            # Configuración de la base de datos
            cls.app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{DB.USER}:{DB.PASS}@{DB.HOST}:{DB.PORT}/{DB.NAME}'
            cls.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

            # COnfiguración de CORS
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
                "error": e
            }), 500)

    @classmethod
    def __register_routes(cls):
        cls.app.add_url_rule(auth["register"], view_func=auth["register_controller"])
        cls.app.add_url_rule(auth["login"], view_func=auth["login_controller"])
