from flask import Blueprint, request 
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.livros import Livro, LivroSchema
from  api.utils.database import db

livro_routes = Blueprint("livro_routes", __name__)

@livro_routes.route('/', methods=['POST'])
def create():
    try:
        data = request.get_json()
        livro_schema = LivroSchema()
        livro = Livro(nome=data["nome"], livros=data["livros"])
        result = livro_schema.dump(livro.create())
        return response_with(resp.SUCCESS_201, 
                            value={"livro":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
    
@livro_routes.route('/', methods=['GET'])
def list():
    fetched = Livro.query.all()
    livro_schema = LivroSchema(many=True, only=['titulo','ano','id'])
    livros, error = livro_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"livros":livros})

livro_routes.route('/<int:autor_id>', methods=['GET'])
def get(autor_id):
    fetched = Livro.query.get_or_404(autor_id)
    livro_schema = LivroSchema()
    livro, error = livro_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"livro":livro})