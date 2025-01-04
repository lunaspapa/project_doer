from .db import db

class Postie(db.Model):
  __tablename__ = 'posties'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  note = db.Column(db.Text, nullable=False)

  user = db.relationship('User', back_populates='posties')

  def to_dict(self):
    return {
      "id": self.id,
      "user_id": self.user_id,
      "note": self.note
    }
