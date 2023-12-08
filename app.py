from flask import Flask, render_template, abort
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BasicConfig
from flask_cors import CORS
from routes.users.users import appuser
from routes.coffees.coffees import appcoffee
from routes.pdf.pdf import apppdf
from routes.csv.csv import appcsv

app = Flask(__name__)
@app.route('/error')
def error():
    abort(404)

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('error.html', error=error), 404

app.register_blueprint(appuser)
app.register_blueprint(appcoffee)
app.register_blueprint(apppdf)
app.register_blueprint(appcsv)
app.config.from_object(BasicConfig)
CORS(app)
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)