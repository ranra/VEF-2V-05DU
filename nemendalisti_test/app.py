"""
Flask - SQLite einfalt sýnidæmi
tutorial: https://www.tutorialspoint.com/flask/flask_sqlite.htm
Python er með innbyggðan stuðning við SQLite
nánar um SQLite: https://www.sqlite.org/
"""

from flask import Flask, render_template, request

# Create an SQLite database ‘database.db’ and create a students’ table in it.
import sqlite3 as sql
app = Flask(__name__)



# student information form.
@app.route('/')
@app.route('/enternew')
def new_student():
   return render_template('student.html')

# retrieves the form’s data by POST method and inserts in students table.
# Message corresponding to success or error in insert operation is rendered to ‘result.html’.
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES(?, ?, ?, ?)",(nm,addr,city,pin) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


# List, populates ‘rows’ as a MultiDict object containing all records in the students table.
# This object is passed to the list.html template.
# entry point to application

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)

if __name__ == '__main__':
   app.run(debug = True)