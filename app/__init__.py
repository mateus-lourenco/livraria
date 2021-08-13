from flask import Flask
from flask_migrate import Migrate
from config import get_config
from .models import configure as config_db
from .serializer import configure as config_ma
from .livro import bp_livro

db_uri = get_config()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    config_db(app)
    config_ma(app)
    
    Migrate(app, app.db)
    
    app.register_blueprint(bp_livro)
    
    return app