import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_bcrypt import Bcrypt

flask_bcrypt = Bcrypt()
db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    flask_bcrypt.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("connection_string", "postgres://postgres:Netsolpk1@127.0.0.1:5432/test") #'sqlite:///' + os.path.join(basedir, 'SIB_main.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app