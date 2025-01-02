from app.models import db, User
from datetime import date
from app.utils import avagen

# Demo User
def seed_users():
  ava_data = avagen()
  demo = User(
    email="demo@doer.com",
    password="mypassword",
    username="demodoer",
    birthday=date(1993, 7, 11),
    avatar=ava_data,
  )

  db.session.add(demo)
  db.session.commit()

def undo_users():
  db.session.execute('TRUNCATE doer_users RESTART IDENTITY CASCADE;')
  db.session.commit()
