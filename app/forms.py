from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login", validators=[DataRequired()])
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError("User not found")



class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField("Phone", validators=[DataRequired(), ])
    email = EmailField("Email", validators=[DataRequired(), ])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register", validators=[DataRequired()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username already taken. Please choose another one")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That Email already taken. Please choose another one")

    # def validate_confirm_password(self, confirm_password):
    #     if self.password.data != confirm_password.data:
    #         raise ValidationError("Password and Confirm Password must be match")



class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=10, max=512)])
    body = TextAreaField("Body", validators=[DataRequired()])
    submit = SubmitField("Create", validators=[DataRequired()])