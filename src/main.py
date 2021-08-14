from flask import Flask
from flask import jsonify
from api.config import config
from api.utils.database import db
from api.utils.responses import response_with
import api.utils.responses as resp

app = Flask(__name__)

app.config.from_object(config.get_config())
    
db.init_app(app)

with app.app_context():
    db.create_all()

# START GLOBAL HTTP CONFIGURATIONS
@app.after_request
def add_header(response):
    return response

@app.errorhandler(400)
def bad_request(e):
    #logging.error(e)
    return response_with(resp.BAD_REQUEST_400)

@app.errorhandler(500)
def server_error(e):
    #logging.error(e)
    return response_with(resp.SERVER_ERROR_500)

@app.errorhandler(404)
def not_found(e):
    #logging.error(e)
    return response_with(resp.SERVER_ERROR_404)

db.init_app(app)

with app.app_context():
    db.create_all()
    
if __name__=="__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)
    