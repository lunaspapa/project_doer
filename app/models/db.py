from flask_sqlalchemy import SQLAlchemy
import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

db = SQLAlchemy()

# Adding prefix for production
def add_prefix_for_prod(attr):
  if environment == "production":
    return f"{SCHEMA}.{attr}"
  else:
    return attr
