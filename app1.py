#!/usr/bin/python3
import sqlite3
from flask import Flask, request, render_template, redirect, url_for, json, jsonify, send_from_directory
app = Flask(__name__)

conn = sqlite3.connect('database.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE students(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     rollno INTEGER,
#     email TEXT,
#     contact INTEGER,
#     branch TEXT,
#     address TEXT
# );''')


conn.commit()

conn.close()
# @app.route("/")
# def mainPage() -> str:
# 	return render_template("home.html")

@app.route('/')
def addPage():
    return render_template("home.html")

@app.route('/students.html')
def students():
    return render_template("students.html")

@app.route('/faculties.html')
def faculties():
    return render_template("faculties.html")

@app.route('/home.html')
def home():
     return render_template("home.html")

# @app.route('/searchStu.html')
# def stuSearch():
#      return render_template("searchStu.html")

# @app.route('/searchFac.html')
# def facSearch():
# #      return render_template("searchFac.html")

@app.route("/students", methods = ['POST'])
def addStudent() -> str:
    data = {"name": "", "email": "", "rollno": "", "contact": "", "program": ""}
    name = request.form.get("name")
    rollno = request.form.get("rollno")
    email = request.form.get("email")
    contact = request.form.get("contact")
    program = request.form.get("branch")  
    
    with sqlite3.connect('database.db') as database:
            cursor = database.cursor()

            query = f"SELECT rollno FROM students WHERE rollno = {rollno}"
            cursor.execute(query)
            data = cursor.fetchall()

            if len(data) != 0:
                return render_template("fail.html")
            else:
                cursor.execute("INSERT INTO students (name, rollno, email, contact, branch) VALUES (?, ?, ?, ?, ?)", (name, rollno, email, contact, program))
                database.commit()

                return render_template("home.html")
            

@app.route("/faculty", methods = ['POST'])
def addfaculty() -> str:
    data = {"name": "",  "faculty_id": "", "email": "", "phone_number": "", "qualifications": ""}
    name = request.form.get("name")
    f_id= request.form.get("faculty_id")
    email = request.form.get("email")
    contact = request.form.get("phone_number")
    qualifications = request.form.get("qualifications")  
    
    with sqlite3.connect('database.db') as database:
            cursor = database.cursor()

            query = f"SELECT rollno FROM students WHERE faculty_id = {f_id}"
            cursor.execute(query)
            data = cursor.fetchall()

            if len(data) != 0:
                return render_template("fail.html")
            else:
                cursor.execute("INSERT INTO students (name, rollno, email, contact, branch) VALUES (?, ?, ?, ?, ?)", (name, f_id, email, contact, qualifications))
                database.commit()

                return render_template("home.html")
            

@app.route('/display.html')
def display():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        return render_template("display.html", students=students)
    
@app.route("/students/delete", methods=["POST"])
def deleteStudent():
    id = request.form.get("id")
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (id,))
        database.commit()
    return redirect(url_for("display"))

@app.route('/display1.html')
def display1():
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("SELECT * FROM faculty")
        s = cursor.fetchall()

        return render_template("display1.html", s=students)
@app.route("/s/delete", methods=["POST"])
def deleteStudent1():
    id = request.form.get("id")
    with sqlite3.connect('database.db') as database:
        cursor = database.cursor()
        cursor.execute("DELETE FROM faculty WHERE id = ?", (id,))
        database.commit()
    return redirect(url_for("display"))



if __name__ == "__main__":
	app.run(debug = True, port=5000)
    