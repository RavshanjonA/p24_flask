import json
import os

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/blog/<pk>")
def blog(pk):
    with open(f"blog{pk}.json") as f:
        data = json.load(f)

    return render_template(f"blog.html", **data)


@app.route("/user/<username>")
def hello(username):
    return f"<h3> Hello {username} </h3>"


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        a1 = request.form.get("a1")
        a2 = request.form.get("a2")
        action = request.form.get("action")
        a1, a2 = int(a1), int(a2)
        match action:
            case "add":
                result = a1 + a2
            case "sub":
                result = a1 - a2
        return render_template("calculate.html", natija=result)


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
