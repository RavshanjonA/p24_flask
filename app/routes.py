from flask import render_template, flash, redirect, url_for, request, session

from app import app, bcrypt, db
from app.forms import RegistrationForm, LoginForm, PostForm
from app.models import User, Post


@app.route("/", )
def home():
    return render_template("home.html", )


@app.route("/login", methods=["POST", "GET"])
def login():
    if session.get("user_id"):
        return redirect(url_for("home"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session["user_id"] = user.id
            session["username"] = user.username
            flash(f"Welcome {user.username}", "success")
            return redirect(url_for("home"))
        else:
            flash("username or password wrong", "danger")

    return render_template("auth/login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get("user_id"):
        return redirect(url_for("home"))
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, password=hashed_password, email=form.email.data,
                    phone=form.phone.data)
        db.session.add(user)
        db.session.commit()
        flash("User  successfully registered", "success")
        return redirect(url_for("login"))

    return render_template("auth/register.html", form=form)


@app.route("/my_blogs")
def my_blog():
    user_id = session.get("user_id")
    posts = Post.query.filter_by(user_id=user_id)
    return render_template("blog/blogs.html", posts=posts)


@app.route("/new_blog", methods=["GET", "POST"])
def new_blog():
    form = PostForm()
    if form.validate_on_submit():
        user_id = session.get("user_id")
        user = User.query.filter_by(id=user_id).first_or_404()
        post = Post(title=form.title.data, body=form.body.data, user_id=user.id)
        db.session.add(post)
        db.session.commit()
        flash("Post Successfully created", "success")
        return redirect(url_for("my_blog"))

    return render_template("blog/new-blog.html", form=form)


@app.route("/log_out")
def log_out():
    session.pop("user_id")
    username = session.pop("username")
    flash(f"{username} user successfully loged out", "success")
    return redirect(url_for("home"))
