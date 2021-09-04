from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp 
from api.models.autores import Autor, AutorSchema
from api.utils.database import db 
from flask_jwt_extended import jwt_required

autor_routes = Blueprint("autor_routes", __name__)

@autor_routes.route("/", methods=["POST"])
@jwt_required
def create():
    try:
        data = request.get_json()
        autor_schema = AutorSchema()
        autor = Autor(nome=data.get("nome"), 
                    livros=data.get("livros"))
        result = autor_schema.dump(autor.create())
        return response_with(resp.SUCCESS_201, 
                            value={"autor":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
    
@autor_routes.route("/", methods=["GET"])
def list():
    fetched = Autor.query.all()
    autor_schema = AutorSchema(many=True, only=["nome","id"])
    autores = autor_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"autores":autores})

@autor_routes.route("/<int:autor_id>", methods=["GET"])
def get(autor_id):
    fetched = Autor.query.get_or_404(autor_id)
    autor_schema = AutorSchema()
    autor = autor_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"autor":autor})

@autor_routes.route("/<int:autor_id>", methods=["PUT"])
@jwt_required
def update(autor_id):
    data = request.get_json()
    get_autor = Autor.query.get_or_404(autor_id)
    get_autor.nome = data["nome"]
    db.session.add(get_autor)
    db.session.commit()
    autor_schema = AutorSchema()
    autor = autor_schema.dump(get_autor)
    return response_with(resp.SUCCESS_200, value={"autor":autor})

@autor_routes.route("/<int:autor_id>", methods=["PATCH"])
@jwt_required
def modify(autor_id):
    data = request.get_json()
    get_autor = Autor.query.get_or_404(autor_id)
    if data.get("nome"):
        get_autor.nome = data["nome"]
    db.session.add(get_autor)
    db.session.commit()
    autor_schema = AutorSchema()
    autor = autor_schema.dump(get_autor)
    return response_with(resp.SUCCESS_200, value={"autor": autor})

@autor_routes.route('/<int:autor_id>', methods=["DELETE"])
@jwt_required
def remove(autor_id):
    get_autor = Autor.query.get_or_404(autor_id)
    db.session.delete(get_autor)
    db.session.commit()
    return response_with(resp.SUCCESS_204)