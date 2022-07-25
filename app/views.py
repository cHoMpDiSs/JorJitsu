from app import app, db 
from flask import render_template, request, jsonify, redirect
from app.models import Student

@app.route("/", methods=["GET"])
def home():
    students = db.session.query(Student.id, Student.name, Student.rank, Student.dob, Student.email).all()
    return render_template("index.html", students=students)

@app.route("/submit", methods=["POST"]) #ADD GET IF DOESNT REFRESH
def submit():
   
    # global_student_object = Student()
    
    
    name = request.form["name"],
    rank = request.form["rank"],
    dob = request.form["dob"],
    email = request.form["email"]
    
    
    s = Student(name,rank,dob,email)
    db.session.add(s)
    db.session.commit()
    
   
     

    response = f"""
    <tr>
        <td>{s.id}</td>
        <td>{s.name}</td>
        <td>{s.rank}</td>
        <td>{s.dob}</td>
        <td>{s.email}</td>
        
       
        <td>
            <button hx-delete="/delete/{s.id}"
                class="btn btn-primary">
                Delete
            </button>
        </td>
    </tr>
    """
    return response    



@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id: int):
    
    s = Student.query.get(id)
    
    db.session.delete(s)  # prepare DELETE statement
    db.session.commit()  # execute DELETE statement
    return " "                            
