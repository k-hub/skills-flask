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


@app.route("/application", methods=["POST"])
def response():
    """Return a response to acknowledge submitted form."""

    first_name = request.form.get("field-firstname")
    last_name = request.form.get("field-lastname")
    salary = request.form.get("field-salary")
    job_title = request.form.get("select-job")

    return render_template("application-response.html",
                            firstname=first_name,
                            lastname=last_name,
                            salary=salary,
                            jobtitle=job_title)


if __name__ == "__main__":
    app.run(debug=True)
