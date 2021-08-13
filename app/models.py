from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Livro(db.Model):
    __tablename__ = 'livros'
    
    id = db.Column(db.Integer())
    isbn = db.Column(db.String())
    titulo = db.Column(db.String())
    autor = db.Column(db.String())
    