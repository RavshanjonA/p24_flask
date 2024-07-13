import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

if not os.path.exists(os.getenv("UPLOAD_FOLDER")):
    os.makedirs(os.getenv("UPLOAD_FOLDER"))


from app import routes
