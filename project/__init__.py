from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'c4aeda7d1114d1a8a7e15ab1'
db = SQLAlchemy(app)


from project import routes
