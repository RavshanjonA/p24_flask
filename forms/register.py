from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField("Phone", validators=[DataRequired(), ])
    email = EmailField("Email", validators=[DataRequired(), ])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Submit", validators=[DataRequired(), EqualTo("password")])

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError("That username already taken. Please choose another one")
    #
    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user:
    #         raise ValidationError("That Email already taken. Please choose another one")

    # def validate_confirm_password(self, confirm_password):
    #     if self.password.data != confirm_password.data:
    #         raise ValidationError("Password and Confirm Password must be match")
