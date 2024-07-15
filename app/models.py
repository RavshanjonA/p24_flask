from slugify import slugify
from sqlalchemy import UniqueConstraint

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(56), unique=True, nullable=False)
    email = db.Column(db.String(56), unique=True, nullable=False)
    phone = db.Column(db.String(24), default="+998991112233")
    password = db.Column(db.String(128), unique=False, nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)
    likes = db.relationship('Like', backref='user', lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    body = db.Column(db.Text())
    image_url = db.Column(db.String(128), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    slug = db.Column(db.String(512), nullable=True)
    likes = db.relationship('Like', backref='post', lazy=True)

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('title', ''), kwargs.get('user_id'))

        super().__init__(*args, **kwargs)


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    __table_args__ = (UniqueConstraint('user_id', 'post_id'),)
