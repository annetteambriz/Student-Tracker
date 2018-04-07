"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def display_home():

    return render_template("home.html")

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)

    return html

@app.route("/add-student")
def show_add_student_form():
    """Show form for to add a student."""

    return render_template("add_student_form.html")


@app.route("/confirm-added", methods=['POST'])
def add_student():
    """Adds a student to our db"""
    # import pdb; pdb.set_trace()
    if request.method == "POST":

        first = request.form.get('first_name')
        last= request.form.get('last_name')
        github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    html = render_template("added_student_confirmation.html",
                            first=first,
                            last=last,
                            github=github)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
