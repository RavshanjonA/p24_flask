import random

from faker import Faker
from slugify import slugify

from app import bcrypt, db
from app.models import User, Post


def generate_user():
    faker = Faker()
    for _ in range(5):
        user = User(username=faker.user_name(), email=faker.email(), phone=faker.phone_number())
        password = faker.password()
        with open("users.txt", "a") as f:
            f.write(f"{user.username} {password}\n")

        user.password = bcrypt.generate_password_hash(password=password).decode("utf-8")
        db.session.add(user)
    db.session.commit()


def generate_post():
    faker = Faker()
    for _ in range(20):
        user_id = random.randint(1, 6)
        user = User.query.filter_by(id=user_id).first()
        post = Post(title=faker.text(), body=faker.paragraph(nb_sentences=random.randint(4, 12)), user_id=user.id)
        db.session.add(post)
    db.session.commit()

def generate_slug_for_exits_posts():
    posts = Post.query.all()
    for post in posts:
        post.slug = slugify(post.title)
        db.session.add(post)
    db.session.commit()