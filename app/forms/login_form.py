from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

def user_exists(form, field):
  email = field.data
  user = User.query.filter(User.email == email).first()
  if not user:
    raise ValidationError("We couldn't find that email.")

def password_match(form, field):
  password = field.data
  email = form.data["email"]
  user = User.query.filter(User.email == email).first()
  if not user:
    raise ValidationError("User does not exist.")
  if not user.check_password(password):
    raise ValidationError("Please try your password again.")

class LoginForm(FlaskForm):
  email = StringField("email", validators=[DataRequired(message="Please enter your email."), Email(message="Please enter a valid email address."), user_exists])
  password = StringField("password", validators=[DataRequired(message="Please enter your password."), password_match])
