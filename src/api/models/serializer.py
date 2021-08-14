from flask_marshmallow import Marshmallow, sqla
from marshmallow import fields
from api.utils.database import db
from .livros import Livro
from .autores import Autor

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class LivroSchema(ma.SQLAlchemyAutoSchema):
    class Meta(ma.SQLAlchemyAutoSchema.Meta):
        model = Livro
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    titulo = fields.String(required=True)
    ano = fields.Integer(required=True)
    autor_id = fields.Integer()

    
class AutorSchema(ma.SQLAlchemyAutoSchema):
    class Meta(ma.SQLAlchemyAutoSchema.Meta):
        model = Autor
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    nome = fields.String(required=True)
    livros = fields.Nested(LivroSchema, many=True,
                        only=['title','year','id'])