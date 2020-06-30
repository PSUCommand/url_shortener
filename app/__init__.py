from flask import Flask
import sqlite3
from contextlib import closing
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

# configuration
DATABASE = os.path.join(PROJECT_ROOT, 'links.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

from app import routes