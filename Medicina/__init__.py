from dotenv import load_dotenv
load_dotenv()
from flask import Flask, redirect
from flask_cors import CORS
from src.routes.public import auth, register
from src.config import APP, DB

app = Flask(__name__)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{DB.USER}:{DB.PASS}@{DB.HOST}:{DB.PORT}/{DB.NAME}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configuración de arranque
app.config["RUN_CONFIG"] = dict(host=APP.HOST, port=APP.PORT, debug=APP.DEBUG)

# Configuración de CORS
CORS(app, resources={
    r"/*": {
        "origins": [APP.CORS, "*"]
    }
}, supports_credentials=True)

# Rutas de login


@app.errorhandler(404)
def notFound(e):
    return redirect("/api/v1/")
