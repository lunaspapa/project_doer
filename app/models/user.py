from .db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), nullable=False)
  hashed_password = db.Column(db.String(255), nullable=False)
  username = db.Column(db.String(30), unique=True, nullable=False)
  avatar = db.Column(db.String(255), default=None)
  birthday = db.Column(db.Date, nullable=False)
  goals_met = db.Column(db.Integer)

  goals = db.relationship('Goal', back_populates='user', cascade='all, delete')
  posties = db.relationship('Postie', back_populates='user', cascade='all, delete')

  @property
  def password(self):
    return self.password

  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.hashed_password, password)

  def is_active(self):
    return True

  def is_authenticated(self):
    return True

  def is_anonymouse(self):
    return False

  def get_id(self):
    return self.id

  def to_dict(self):
    return {
      'id': self.id,
      'email': self.email,
      'username': self.username,
      'avatar': self.avatar,
      'birthday': self.birthday,
      'goals_met': self.goals_met
    }
