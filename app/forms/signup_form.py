# FlaskWTF
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from app.models import User

# Check if user already exists
def user_exists(form, field):
  email = field.data
  user = User.query.filter(User.email == email).first()
  if user:
    raise ValidationError("Email address is already in use.")

# Check if a username is taken
def username_taken(form, field):
  username = field.data
  user = User.query.filter(User.username == username).first()
  if user:
    raise ValidationError("Username has been taken.")

class SignUpForm(FlaskForm):
  email = StringField("email", validators=[DataRequired(message="Please provide an email."), Email(message="Please provide a valid email address."), user_exists])
  username = StringField("username", validators=[DataRequired(message="Please enter your desired username."), username_taken])
  password = StringField("password", validators=[DataRequired(message="Please enter a strong password.")])
  birthday = DateField("birthday", validators=[DataRequired(message="Please enter your birthday. (We want to celebrate you!)")])
