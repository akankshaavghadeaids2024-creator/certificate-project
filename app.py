from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    name = request.form.get("name", "").strip()
    roll = request.form.get("roll", "").strip()

    if not name and not roll:
        return "Please enter a name or roll number.", 400

    today = date.today().strftime("%d %B %Y")
    return render_template("certificate.html", name=name, roll=roll, today=today)


if __name__ == "__main__":
    app.run(debug=True)