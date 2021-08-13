from flask_marshmallow import Marshmallow
from .models import Livro

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class LivroSchema(ma.SQLAlchemyAutoSchema):
    class Meta():
        model = Livro