from flask import Flask
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config.from_mapping(
    DATABASE = os.path.join(PROJECT_ROOT, 'links.db'),
    DEBUG = True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default'
)

from . import db
db.init_app(app)

from app import routes