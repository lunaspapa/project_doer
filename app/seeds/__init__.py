from flask.cli import AppGroup
from .users import seed_users, undo_users
from .goals import seed_goals, undo_goals
from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
  if environment == "production":
    db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    db.session.execute(f"TRUNCATE table {SCHEMA}.goals RESTART IDENTITY CASCADE;")
    db.session.execute(f"TRUNCATE table {SCHEMA}.subgoals RESTART IDENTITY CASCADE;")
    db.session.execute(f"TRUNCATE table {SCHEMA}.minigoals RESTART IDENTITY CASCADE;")

    db.session.commit()

  seed_users()
  seed_goals()

@seed_commands.command('undo')
def undo():
  undo_users()
  undo_goals()
