# LIVRARIA API

EXEMPLO DE API FLASK COM CRUD

## COMO EXECUTAR

### SETUP DE AMBIENTE

``` sh
python -m virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```
### VARIÁVEIS DE AMBIENTE

``` sh
export FLASK_APP=app
export FLASK_ENV=development
export DATABASE_URL="sqlite:////tmp/test.db"
```