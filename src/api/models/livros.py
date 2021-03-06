from api.utils.database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

class Livro(db.Model):
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50))
    ano_publicacao = db.Column(db.Integer)
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.id'))

    def __init__(self, titulo, ano, autor_id=None):
        self.titulo = titulo
        self.ano = ano
        self.autor_id = autor_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
class LivroSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Livro
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    titulo = fields.String(required=True)
    ano = fields.Integer(required=True)
    autor_id = fields.Integer()

