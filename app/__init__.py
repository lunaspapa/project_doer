import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .models import User

from .config import Config

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

# Set up login manager
login = LoginManager(app)
login.login_view = "auth.unauthorized"

@login.user_loader
def load_user(id):
  return User.query.get(int(id))
