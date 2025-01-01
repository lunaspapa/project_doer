from app.models import db, User
from datetime import date

# Demo User
def seed_users():
  demo = User(
    email="demo@doer.com",
    password="mypassword",
    username="demodoer",
    birthday=date(1993, 7, 11)
  )

  db.session.add(demo)
  db.session.commit()

def undo_users():
  db.session.execute('TRUNCATE doer_users RESTART IDENTITY CASCADE;')
  db.session.commit()
