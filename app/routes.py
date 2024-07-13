import os

from flask import render_template, flash, redirect, url_for, request, session

from app import app, bcrypt, db
from app.decorators import login_required
from app.forms import RegistrationForm, LoginForm, PostForm
from app.models import User, Post
from app.utils import generate_image_url


@app.route("/", )
@login_required(required=True)
def home():
    return render_template("home.html", )


@app.route("/login", methods=["POST", "GET"])
@login_required(required=False)
def login():
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
@login_required(required=False)
def register():
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
@login_required(required=True)
def my_blog():
    user_id = session.get("user_id")
    posts = Post.query.filter_by(user_id=user_id)
    return render_template("blog/blogs.html", posts=posts)


@app.route("/blog_detial/<pk>")
@login_required(required=True)
def blog_detial(pk):
    post = Post.query.filter_by(id=pk).first()
    return render_template("blog/blog.html", post=post)


@app.route("/new_blog", methods=["GET", "POST"])
@login_required(required=True)
def new_blog():
    form = PostForm()
    if form.validate_on_submit():
        user_id = session.get("user_id")
        image_data = form.image.data
        name: str = image_data.filename
        name, ext = name.rsplit(".", maxsplit=1)
        image_path = generate_image_url(name, ext)
        image_url = f'app/{image_path}'
        image_data.save(image_url)
        user = User.query.filter_by(id=user_id).first_or_404()
        post = Post(title=form.title.data, body=form.body.data, user_id=user.id, image_url=image_path)
        db.session.add(post)
        db.session.commit()
        flash("Post Successfully created", "success")
        return redirect(url_for("my_blog"))

    return render_template("blog/new-blog.html", form=form)


@app.route("/log_out")
@login_required(required=True)
def log_out():
    session.pop("user_id")
    username = session.pop("username")
    flash(f"{username} user successfully loged out", "info")
    return redirect(url_for("home"))
