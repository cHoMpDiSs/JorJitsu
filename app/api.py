from app import app, db 
from flask import render_template, request, jsonify, redirect
from app.models import Student


# this API returns all studunts in JSON 
@app.route('/show', methods=['GET'])
def show():
    students = Student.query.all()
    results = []
    for s in students:
        results.append(s.serialize())  
    return jsonify(results)
    


