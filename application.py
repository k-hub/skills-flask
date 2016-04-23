from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show application form."""

    return render_template("application-form.html")


@app.route("/application")
def response():
    """Return a response to acknowledge submitted form."""

    first_name = request.args.get("firstname")
    last_name = request.args.get("lastname")
    salary = request.args.get("salary")
    job_title = request.args.get("jobtitle")

    return render_template("application-response.html",
                            firstname=first_name,
                            lastname=last_name,
                            salary=salary,
                            jobtitle=job_title)


if __name__ == "__main__":
    app.run(debug=True)
