from flask import Flask
from flask_cors import CORS
from src.routes.public import auth, register
from src.config import APP, DB

class Application():

    @classmethod
    def create_app(cls):
        cls.app = Flask(__name__)
        cls.__configure()
        return cls.app

    @classmethod
    def __configure(cls):
    # Configuración de la base de datos
        cls.app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{DB.USER}:{DB.PASS}@{DB.HOST}:{DB.PORT}/{DB.NAME}'
        cls.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        # Configuración de arranque
        cls.app.config["RUN_CONFIG"] = dict(host=APP.HOST, port=APP.PORT, debug=APP.DEBUG)

        # Configuración de CORS
        CORS(cls.app, resources={
            r"/*": {
                "origins": [APP.CORS, "*"]
            }
        }, supports_credentials=True)

        cls.__register_routes()
