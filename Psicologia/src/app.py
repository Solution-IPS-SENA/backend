from flask import Flask
from flask_cors import CORS
from src.routes.public import routes
from src.config import APP, DB, REDIS

class Application():

    @classmethod
    def create_app(cls):
        cls.app = Flask(__name__)
        cls.__configure()
        cls.__register_routes()
        return cls.app

    @classmethod
    def __configure(cls):
        # Configuración de la base de datos
        cls.app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{DB.USER}:{DB.PASS}@{DB.HOST}:{DB.PORT}/{DB.NAME}'
        cls.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        # Configuración de redis
        cls.app.config["REDIS_URL"] = f"redis://:@{REDIS.HOST}:{REDIS.PORT}/{REDIS.DB_NUMBER}"
        # Configuración de arranque
        cls.app.config["RUN_CONFIG"] = dict(host=APP.HOST, port=APP.PORT, debug=APP.DEBUG)

        # Configuración de CORS
        CORS(cls.app, resources={
            r"/*": {
                "origins": [APP.CORS, "*"]
            }
        }, supports_credentials=True)

    @classmethod
    def __register_routes(cls):
        cls.app.add_url_rule(routes["historia_psicologia"], view_func=routes["historia_psicologia_controller"], methods=["GET", "POST", "PUT"])