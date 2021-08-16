from flask import Blueprint, request 
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.livros import Livro, LivroSchema
from  api.utils.database import db

livro_routes = Blueprint("livro_routes", __name__)

