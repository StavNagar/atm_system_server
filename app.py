from flask import Flask
from flask_jwt_extended import JWTManager
from src.auth import auth_bp
from src.services import account_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(account_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)