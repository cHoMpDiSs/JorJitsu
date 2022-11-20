from app import db
from datetime import datetime


class Student(db.Model):

    __tablename__='student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)  
    rank = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.String)
    email = db.Column(db.String(40), unique=True,nullable=True)

    def __init__(self, name: str, rank: str, dob: str, email: str):
        
        self.name = name
        self.rank = rank
        self.dob = dob
        self.email = email
        

    def __repr__(self):
        return f'Student("{self.name}","{self.rank}",{self.dob}, {self.email})'


class Academy(db.Model):

    __tablename__= 'academy'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    a_professer = db.relationship('Professor', backref='Academy')
    kids_class = db.Column(db.Boolean, default=False, nullable=True)
    
   
    def __init__(self, city: str, id: int):
        self.city = city
        self.id = id

    def __repr__(self):
        return '<Academy: {}>'.format(self.name)

class Professor(db.Model):
    
    __tablename__= 'professor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    rank = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime)
    academy_id = db.Column(db.Integer, db.ForeignKey('academy.id'), nullable=False)
    teaches = db.relationship('Academy', backref='professor')

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __repr__(self):
        return '<Professor: {}>'.format(self.name)



class Account(db.Model):

    __tablename__='account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username: str, password: str, id: int):
        self.username = username
        self.password = password
        self.id = id
