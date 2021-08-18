from api.utils.database import db
from api.models.livros import LivroSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from marshmallow import fields

class Autor(db.Model):
    __tablename__ = 'autores'

    id = db.Column(db.Integer, primary_key=True,
                autoincrement=True)
    nome = db.Column(db.String(100))
    created = db.Column(db.DateTime, server_default=db.func.now())
    livros = db.relationship('Livro', backref='Autor',
                            cascade="all, delete-orphan")

    def __init__(self, nome, livros=list()):
        self.nome = nome
        self.livros = livros

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class AutorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Autor
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    nome = fields.String(required=True)
    created = fields.String(dump_only=True)
    livros = fields.Nested(LivroSchema, many=True,
                        only=['titulo', 'ano', 'id'])
