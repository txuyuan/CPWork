from flask import Flask, render_template, request, redirect 
import sqlite3

ATTRIBUTES = [
    "name",
    "sex",
    "age", 
    "fee",
    "species",
    "writeup"
]

DB_FILE = "db/pet.db"

app = Flask(__name__)

@app.route("/")
@app.route("/<species>")
def query(species=""):
    # TODO: use params for filter
    con, cur = getCursors()

    if species == "":
        cmd = "SELECT * FROM PET"
        print("blank species query")
        cur.execute(cmd)
    else:
        cmd = "SELECT * FROM PET WHERE SPECIES = ?"
        cur.execute(cmd, (species,))

    pets = cur.fetchall()

    cur.close()
    con.close()

    return render_template("query.html", pets=pets)

@app.route('/post')
def post():
    form = request.form
    # add pet_id 
    # verify all values present
    # insert into table
    # return to home

@app.route("/edit/<petId>", methods=['GET', 'POST'])
def edit(petId):
    con, cur = getCursors()
    if request.method == "GET":

        cmd = "SELECT * FROM PET WHERE pet_id=?"
        cur.execute(cmd, (petId,))
        results = cur.fetchall()

        if len(results) == 0:
            return render_template("error.html", msg=f"No pet with id {petId} found!")
        elif len(results) > 1:
            return render_template("error.html", msg=f"Multiple pets with this id found!")
    
        pet = results[0]
        return render_template("edit.html", pet=pet)
    elif request.method == "POST":
        pet_id = request.form["pet_id"]
        number = request.form["number"]

        cmd = "SELECT number FROM PET WHERE pet_id = ?"
        cur.execute(cmd, (pet_id,))
        results = cur.fetchall()
        authNumber = results[0]["number"]

        if number == authNumber:
            # Correct, pupdate database

            cmd = """
            UPDATE pet 
            SET {} = ?,
                {} = ?,
                {} = ?,
                {} = ?,
                {} = ?,
                {} = ?
            WHERE pet_id = ?
            """.format(*ATTRIBUTES)

            values = tuple([request.form[attr] for attr in ATTRIBUTES] + [pet_id])
            cur.execute(cmd, values)
            con.commit()

            return redirect("/", code=200)
        else:
            return render_template("editError.html", msg="Incorrect Number", return_url="")

    cur.close()
    con.close()

    

def getCursors():
    con = sqlite3.connect(DB_FILE)
    con.row_factory = sqlite3.Row 
    cur = con.cursor() 

    return (con,cur)

if __name__=="__main__":
    app.run(port=3000)
