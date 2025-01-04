from app.models import db, Postie

def seed_posties():
  demo_postie = Postie(
    user_id=1,
    note="You're doing this for your family."
  )

  db.session.add(demo_postie)
  db.session.commit()

def undo_posties():
  db.session.execute('TRUNCATE posties RESTART IDENTITY CASCADE;')
