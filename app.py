from flask import Flask, request, render_template, flash, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
import forms
import models


@app.route("/", )
def home():
    return render_template("home.html", )


@app.route("/login", )
def login():
    return render_template("auth/login.html", )


@app.route("/register", methods=["GET", "POST"])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = models.User(username=form.username.data, password=hashed_password, email=form.email.data,
                           phone=form.phone.data)
        db.session.add(user)
        db.session.commit()
        flash("User  successfully registered", "success")
        return redirect(url_for("login"))
    return render_template("auth/register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
