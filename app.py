import sqlite3
import random
from flask import Flask, redirect, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "iosdhnj;osdnuijsab"


@app.route("/", methods=["POST", "GET"])
def index():
    if ("all_items" not in session or "shopping_items" not in session):
        session["all_items"], session["shopping_items"] = get_db()
    return render_template("index.html", all_items=session["all_items"],
                           shopping_items=session["shopping_items"])


@app.route("/add_items", methods=["post"])
def add_items():
    session["shopping_items"].append(request.form["new-item"])
    session.modified = True
    session["shopping_items"] = sorted(session["shopping_items"])
    return redirect(request.referrer)


@app.route("/remove_items", methods=["post"])
def remove_items():
    checked_boxes = request.form.getlist("check")
    for item in checked_boxes:
        if item in session["shopping_items"]:
            idx = session["shopping_items"].index(item)
            session["shopping_items"].pop(idx)
            session.modified = True
    return redirect(request.referrer)


# Connection SQLite database to our application
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        # FIXME If no grocery_list.db, run generate_grocery_list.py
        db = g._database = sqlite3.connect('grocery_list.db')
        cursor = db.cursor()
        cursor.execute("select name from groceries")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]

        shopping_list = all_data.copy()
        random.shuffle(shopping_list)
        shopping_list = sorted(shopping_list[:5])
    return all_data, shopping_list


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
