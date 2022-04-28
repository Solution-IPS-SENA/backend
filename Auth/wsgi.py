from __init__ import app
from src.utils.instances import db

if __name__ == '__main__':
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(**app.config["RUN_CONFIG"])
