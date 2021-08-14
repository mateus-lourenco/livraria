from api.utils.database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .livros import Livro

class Autor(db.Model):
    __tablename__ = 'autores'
    
    id = db.Column(db.Integer, primary_key=True, 
                autorincrement=True)
    nome = db.Column(db.String(100))
    livros = db.relationship('Livro', backref='Autor',
                            cascade="all, delete-orphan")
    
    def __init__(self, nome, livros=[]):
        self.nome = nome
        self.livros = livros
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self