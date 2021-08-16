from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp 
from api.models.autores import Autor, AutorSchema
from api.utils.database import db 

autor_routes = Blueprint("autor_routes", __name__)

@autor_routes.route('/', methods=['POST'])
def create():
    try:
        data = request.get_json()
        autor_schema = AutorSchema()
        autor, error = autor_schema.load(data)
        result = autor_schema.dump(autor.create()).data
        return response_with(resp.SUCCESS_201, 
                            value={"autor":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
    
@autor_routes.route('/', methods=['GET'])
def list():
    fetched = Autor.query.all()
    autor_schema = AutorSchema(many=True, only=['first_name',
                                                'last_name','id'])
    autores, error = autor_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"autores":autores})

autor_routes.route('/<int:autor_id>', methods=['GET'])
def get(autor_id):
    fetched = Autor.query.get_or_404(autor_id)
    autor_schema = AutorSchema()
    autor, error = autor_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"autor":autor})

