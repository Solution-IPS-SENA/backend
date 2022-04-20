from flask import Flask, make_response, jsonify
from flask_cors import CORS
from src.routes.routes import routes
from src.config import DB, APP

class Aplication:
    @classmethod
    def create_app(cls):
        cls.app = Flask(__name__)
        cls.__configure()
        return cls.app

    @classmethod
    def __configure(cls):
        try:
            # Database configuration
            cls.app.config["SQLALCHEMY_DATABASE_URI"] = f'{DB.ENGINE}+{DB.DRIVER}://{DB.USER}:{DB.PASS}@{DB.HOST}:{DB.PORT}/{DB.NAME}'
            cls.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

            # CORS configuration
            CORS(cls.app, resources={
               r"/*": {
                   "origins": [APP.CORS, "*"]
               }
            }, supports_credentials=True)

            # Register routes
            cls.__register_routes()

        except Exception as e:
            return make_response(jsonify({
                "response": "Error starting server",
                "error": str(e)
            }), 500)

    @classmethod
    def __register_routes(cls):
        # Rutas
        cls.app.add_url_rule(routes["route_path"], view_func=routes["route_controller"], methods=["POST, GET, PUT, PATCH, DELETE"])
        pass
