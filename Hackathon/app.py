from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students_faculty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_no = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    branch = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    faculty_id = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    
@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        name = request.form['name']
        roll_no = request.form['roll_no']
        email = request.form['email']
        contact = request.form['contact']
        branch = request.form['branch']
        address = request.form['address']
        student = Student(name=name, roll_no=roll_no, email=email, contact=contact, branch=branch, address=address)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('students'))
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/faculties', methods=['GET', 'POST'])
def faculties():
    if request.method == 'POST':
        name = request.form['name']
        faculty_id = request.form['faculty_id']
        email = request.form['email']
        contact = request.form['contact']
        address = request.form['address']
        faculty = Faculty(name=name, faculty_id=faculty_id, email=email, contact=contact, address=address)
        db.session.add(faculty)
        db.session.commit()
        return redirect(url_for('faculties'))
    faculties = Faculty.query.all()
    return render_template('faculties.html', faculties=faculties)

@app.route('/students/<int:id>/edit', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.roll_no = request.form['roll_no']
        student.email = request.form['email']
        student.contact = request.form['contact']
        student.branch = request.form['branch']
        student.address = request.form['address']
        db.session.commit()
        return redirect(url_for('students'))
    return render_template('edit_student.html', student=student)

@app.route('/faculties/<int:id>/edit', methods=['GET', 'POST'])
def edit_faculty(id):
    faculty = Faculty.query.get(id)
    if request.method == 'POST':
        faculty.name = request.form['name']
        faculty.faculty_id = request.form['faculty_id']
        faculty.email = request.form['email']
        faculty.contact = request.form['contact']
        faculty.address = request.form['address']
        db.session.commit()
        return redirect(url_for('faculties'))
    return render_template('edit_faculty.html', faculties=faculties)
if __name__ == '__main__':
    app.run(debug=True)
