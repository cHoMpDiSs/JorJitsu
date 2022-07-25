from app import app
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

if __name__ == "__main__":
    
    app.run(debug=True)