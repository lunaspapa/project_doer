import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .models import db, User, Goal, Subgoal, Minigoal, Postie

from .config import Config

from .seeds import seed_commands

from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.goal_routes import goal_routes
from .api.postie_routes import postie_routes

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

# Set up login manager
login = LoginManager(app)
login.login_view = "auth.unauthorized"

@login.user_loader
def load_user(id):
  return User.query.get(int(id))

app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(goal_routes, url_prefix='/api/goals')
app.register_blueprint(postie_routes, url_prefix='/api/posties')
# More Routes Here
db.init_app(app)
Migrate(app, db)

# Security
CORS(app)

@app.before_request
def https_redirect():
  if os.environ.get('FLASK_ENV') == 'production':
    if request.headers.get('X-Forwarded-Proto') == 'http':
      url = request.url.replace('http://', 'https://', 1)
      code = 301
      return redirect(url, code=code)

@app.after_request
def inject_csrf_token(response):
  response.set_cookie(
    'csrf_token',
    generate_csrf(),
    secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
    samesite='Strict' if os.environ.get('FLASK_ENV') == 'production' else None,
    httponly=True
  )
  return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
  if path == 'favicon.ico':
    return app.send_static_file('public', 'favicon.ico')
  return app.send_static_file('index.html')
