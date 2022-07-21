from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

from utils import db
from config import config


app = Flask(__name__)
#conexion = MySQL(app)

from routes.books import books
from routes.members import members

app.register_blueprint(books)
app.register_blueprint(members)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Qwerty.123@localhost/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)



def page_not_found(error):
    return "<h1>Page does not found! </h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()