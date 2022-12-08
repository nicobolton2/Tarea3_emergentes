from flask import Flask
from DataBase import db
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tables.db'
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app


