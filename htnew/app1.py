#!/usr/bin/python3
import sqlite3
from flask import Flask, request, render_template, redirect, url_for, json, jsonify, send_from_directory
app = Flask(__name__)

conn = sqlite3.connect('database.db')

cursor = conn.cursor()
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
@app.route('/search1.html')
def search1():
    return render_template("search1.html")
@app.route('/faculties.html')
def faculties():
    return render_template("faculties.html")
# @app.route('/SearchPage.html')
# def searchPageRelay():
#      return render_template("SearchPage.html")

# @app.route('/searchStu.html')
# def stuSearch():
#      return render_template("searchStu.html")

# @app.route('/searchFac.html')
# def facSearch():
# #      return render_template("searchFac.html")

@app.route("/students", methods = ['POST'])
def addStudent() -> str:
    data = {"name": "", "email": "", "rollno": "", "contact": "", "program": "", "address": ""}
    name = request.form.get("name")
    rollno = request.form.get("rollno")
    email = request.form.get("email")
    contact = request.form.get("contact")
    program = request.form.get("branch")
    address = request.form.get("address")    
    
    with sqlite3.connect('database.db') as database:
            cursor = database.cursor()

            query = f"SELECT rollno FROM students WHERE rollno = {rollno}"
            cursor.execute(query)
            data = cursor.fetchall()

            if len(data) != 0:
                return render_template("fail.html")
            else:
                cursor.execute("INSERT INTO students (name, rollno, email, contact, branch, address) VALUES (?, ?, ?, ?, ?, ?)", (name, rollno, email, contact, program, address))
                database.commit()

                return render_template("students.html")
            
# @app.route('/search', methods=['POST'])
# def search():
#         name = request.form['name']
#         conn = sqlite3.connect('database.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM students WHERE name=?", (name,))
#         result = cursor.fetchone()
#         conn.close()
#         if result:
#             return render_template('search.html', data=result)
#         else:
#             return render_template('search.html')
@app.route('/search1', methods=[ 'POST'])
def search():
    
        name = request.form['name']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name=?", (name,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return render_template('search1.html', data=result)
        else:
            return render_template('search1.html')



if __name__ == "__main__":
	app.run(debug = True)