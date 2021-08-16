import logging
import sys
from flask import Flask
from flask import jsonify
from api.config import config
from api.utils.database import db
from api.utils.responses import response_with
import api.utils.responses as resp
from api.utils.serializer import ma
from flask_migrate import Migrate
from api.routes.autores import autor_routes
from api.routes.livros import livro_routes

app = Flask(__name__)

app.config.from_object(config.get_config())
    
db.init_app(app)
ma.init_app(app)

app.db = db

Migrate(app, app.db)

with app.app_context():
    db.create_all()
    
app.register_blueprint(autor_routes, url_prefix='/api/autores')
app.register_blueprint(livro_routes, url_prefix='/api/livros')

# START GLOBAL HTTP CONFIGURATIONS
@app.after_request
def add_header(response):
    return response

@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)

@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)

@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)

if __name__=="__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)
    