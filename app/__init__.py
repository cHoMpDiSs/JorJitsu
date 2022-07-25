from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)





app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///jorjitsu'
app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from app import views
from app import models

db.init_app(app)
db.create_all()


