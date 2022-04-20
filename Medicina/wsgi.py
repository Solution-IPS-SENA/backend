from dotenv import load_dotenv

load_dotenv()

from src.app import Aplication
from src.utils.db import db
from flask_sqlalchemy import SQLAlchemy
from src.config import APP

app = Aplication.create_app()

SQLAlchemy(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(APP.HOST, APP.PORT, APP.DEBUG)
