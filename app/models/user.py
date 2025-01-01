from .db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), nullable=False)
  password = db.Column(db.String(20), nullable=False)
  username = db.Column(db.String(30), unique=True, nullable=False)
  avatar = db.Column(db.String(255))
  birthday = db.Column(db.Date, nullable=False)
  goals_met = db.Column(db.Integer, nullable=False)

  @property
  def password(self):
    return self.password

  @password.setter
  def password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def to_dict(self):
    return {
      'id': self.id,
      'email': self.email,
      'username': self.username,
      'avatar': self.avatar,
      'birthday': self.birthday,
      'goals_met': self.goals_met
    }
