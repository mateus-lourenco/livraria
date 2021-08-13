from flask import Blueprint

bp_livro = Blueprint('livro', __name__)

bp_livro.route('/', methods=['POST'])
def create():
    ...

bp_livro.route('/<id>', methods=['PUT'])
def update(id):
    ...

bp_livro.route('/', methods=['GET'])
def list():
    ...
    
bp_livro.route('/<id>', methods=['GET'])
def get(id):
    ...
    
bp_livro.route('/<id>', methods=['DELETE'])
def delete(id):
    ...