import json
import os

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/blog/<pk>")
def blog_detail(pk):
    with open(f"db/blog{pk}.json", "r") as f:
        data = json.load(f)
    return render_template("blog.html", **data)


@app.route("/blogs")
def blogs():
    c = len(os.listdir("db"))
    return render_template("blogs.html", count=c)


@app.route("/user/<username>")
def hello(username):
    return f"<h3> Hello {username} </h3>"

@app.route("/new-blog", methods=("GET", "POST"))
def new_blog():
    if request.method == "GET":
        return render_template("new-blog.html")
    else:
        title = request.form.get("title")
        body = request.form.get("body")
        data = {
            "title": title,
            "body": body
        }
        c = len(os.listdir("db"))
        with open(f"db/blog{c + 1}.json", "w") as f:
            json.dump(data, f)
        message = "Blog successfully created"
        c += 1
        return render_template("blogs.html", message=message, count=c)


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
