from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(56), unique=True, nullable=False)
    email = db.Column(db.String(56), unique=True, nullable=False)
    phone = db.Column(db.String(24), default="+998991112233")
    password = db.Column(db.String(128), unique=False, nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)
    body = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
