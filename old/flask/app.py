from flask import Flask, render_template, request
import sqlite3

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()
c.execute('''CREATE TABLE mytablers (rollNo INTEGER PRIMARY KEY, name TEXT, phone INTEGER, branch TEXT )''')
conn.commit()
conn.close()

app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM mytablers')
    rows = c.fetchall()
    conn.close()
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('INSERT INTO mytablers (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()
    return redirect('/')
    return 'Data added to database'


@app.route('/display')
def display():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM mytablers')
    rows = c.fetchall()
    conn.close()
    return render_template('display.html', rows=rows)
