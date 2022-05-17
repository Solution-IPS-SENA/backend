import __init__
from src.app import Application
from src.utils.instances import db, rd

app = Application.create_app()

if __name__ == '__main__':
    
    try:
        db.init_app(app)
        rd.init_app(app)
        with app.app_context():
            db.create_all()
        app.run(**app.config["RUN_CONFIG"])

    except Exception as e:
        print(f"Error starting server: {e}")
