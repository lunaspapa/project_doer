from flask import Blueprint, jsonify, session, request
from app.models import db, User
from app.forms import LoginForm, SignUpForm
from app.utils import avatar_gen
from flask_login import current_user, login_user, logout_user, login_required

auth_routes = Blueprint("auth", __name__)

# Validation errors to List
def validation_error_output(validation_errors):
  errorMessages = []
  for field in validation_errors:
    for error in validation_errors[field]:
      errorMessages.append(f"{error}")
  return errorMessages

@auth_routes.route("/")
def authenticate():
  if current_user.is_authenticated:
    return current_user.to_dict()
  return {'errors': ["Unauthorized"]}

@auth_routes.route("/login",methods=["POST"])
def login():
  form = LoginForm()
  form["csrf_token"].data = request.cookies["csrf_token"]
  if form.validate_on_submit():
    user = User.query.filter(User.email == form.data["email"]).first()
    login_user(user)
    print('WE HERE')
    return user.to_dict()
  return {"errors": validation_error_output(form.errors)}, 401

@auth_routes.route("/logout")
def logout():
  logout_user()
  return {"message": "User logged out"}

@auth_routes.route("/signup",methods=["POST"])
def signup():
  form = SignUpForm()
  form["csrf_token"].data = request.cookies["csrf_token"]
  if form.validate_on_submit():
    avatar_data = avatar_gen()
    user = User(
      email=form.data["email"],
      username=form.data["username"],
      hashed_password=form.data["password"],
      birthday=form.data["birthday"],
      avatar=avatar_data
    )

    db.session.add(user)
    db.session.commit()
    login_user(user)
    return user.to_dict()
  print({"errors": validation_error_output(form.errors)})
  return {"errors": validation_error_output(form.errors)}, 401

@auth_routes.route("/unauthorized")
def unauthorized():
  return {"errors": ["Unauthorized"]}, 401
