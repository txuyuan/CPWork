from flask import Flask, request, url_for, render_template
import sqlite3

app = Flask(__name__)

def get_records():
    con = sqlite3.connect("../students.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("""
        SELECT Student.Name, Student.Gender, Record.Weight, Record.Height
        FROM Student
        OUTER LEFT JOIN StudentHealthRecord Record ON Student.StudentID = Record.StudentID
        ORDER BY  Student.Gender ASC, Student.Name DESC
                """) 
    results = cur.fetchall()

    cur.close()
    con.close()
    return results

def get_statistics():
    con = sqlite3.connect("../students.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("""
        SELECT Student.Gender, COUNT(*) AS Total, AVG(Record.Weight) AS Weight, AVG(Record.Height) AS Height
        FROM Student
        OUTER LEFT JOIN StudentHealthRecord Record ON Student.StudentID = Record.StudentID
        GROUP BY Student.Gender
                """)
    results = cur.fetchall()

    cur.close()
    con.close()
    return results

def insert_student(studentID, height, weight):
    con = sqlite3.connect("../students.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("""
        INSERT INTO StudentHealthRecord(StudentID, Weight, Height)
        VALUES(?, ?, ?)
                """, (studentID, height, weight))
    con.commit()
    cur.close()
    con.close()

@app.route("/")
def index():
    return render_template("menu.html")

@app.route("/records")
def records():
    records = get_records()
    return render_template("records.html", records=records)

@app.route("/statistics")
def statistics():
    statistics = get_statistics()
    return render_template("statistics.html", statistics=statistics)

@app.route("/add_record", methods=["GET", "POST"])
def add_record():
    if request.method == "POST":
        studentID, height, weight = request.form["studentID"], request.form["height"], request.form["weight"]
        insert_student(studentID, height, weight)
        return "Request Sent!"
    else:
        return render_template("add_record.html")

if __name__ == "__main__":
    app.run()
