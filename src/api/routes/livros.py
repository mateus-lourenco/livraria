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
        livro = livro_schema.load(data)
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

@livro_routes.route('/<int:autor_id>', methods=['GET'])
def get(autor_id):
    fetched = Livro.query.get_or_404(autor_id)
    livro_schema = LivroSchema()
    livro, error = livro_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"livro":livro})

@livro_routes.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    get_livro = Livro.query.get_or_404(id)
    get_livro.titulo = data['titulo']
    get_livro.ano = data['ano']
    db.session.add(get_livro)
    db.session.commit()
    livro_schema = LivroSchema()
    livro = livro_schema.dump(get_livro)
    return response_with(resp.SUCCESS_200, value={"livro": livro})

@livro_routes.route('/<int:id>', methods=['PATCH'])
def modify(id):
    data = request.get_json()
    get_livro = Livro.query.get_or_404(id)
    if data.get('titulo'):
        get_livro.titulo = data['titulo']
    if data.get('ano'):
        get_livro.ano = data['ano']
    db.session.add(get_livro)
    db.session.commit()
    livro_schema = LivroSchema()
    livro = livro_schema.dump(get_livro)
    return response_with(resp.SUCCESS_200, value={"livro": livro})

@livro_routes.route('/<int:id>', methods=['DELETE'])
def delete(id):
    get_livro = Livro.query.get_or_404(id)
    db.session.delete(get_livro)
    db.session.commit()
    return response_with(resp.SUCCESS_204)