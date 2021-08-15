from api.utils.database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from api.models.livros import LivroSchema


class Autor(db.Model):
    __tablename__ = 'autores'

    id = db.Column(db.Integer, primary_key=True,
                autoincrement=True)
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


class AutorSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Autor
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    nome = fields.String(required=True)
    livros = fields.Nested(LivroSchema, many=True,
                        only=['titulo', 'ano', 'id'])
