from flask import Flask
from flask_migrate import Migrate
from api.config import config
from api.utils.database import db
#from .models import configure as config_db
#from .serializer import configure as config_ma
#from .livro import bp_livro

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    
    Migrate(app, app.db)
    
    #app.register_blueprint(bp_livro)
    with app.app_context():
        db.create_all()
    
    return app
    
if __name__=="__main__":
    create_app.run(port=5000, host="0.0.0.0", use_reloader=False)
    