from flask import Flask, render_template, url_for, redirect, request
import sqlite3

app = Flask(__name__)

def fetch_donuts(date):
    con = sqlite3.connect("../donut_store.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("""
        SELECT Donut.DonutName AS name, COUNT(*) AS count
        FROM Sale
        INNER JOIN Donut ON Sale.DonutID = Donut.DonutID
        WHERE Sale.Date = ?
        GROUP BY Sale.DonutID
        ORDER BY COUNT(*) DESC
                """.strip(), (date,))
    results = cur.fetchall()

    cur.close()
    con.close()
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("form.html")
    else:
        date = request.form["date_string"].replace("-", "")
        donuts = [(donut["name"], donut["count"]) for donut in fetch_donuts(date)]
        return render_template("donuts.html", date=date, donuts=donuts)


if __name__ == "__main__":
    app.run()
