from .db import db

class Goal(db.Model):
  __tablename__ = "goals"

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db. ForeignKey('users.id'))
  category = db.Column(db.String, nullable=True)
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String)
  meetline = db.Column(db.Date, default=None)
  is_daily = db.Column(db.Boolean, default=False, nullable=False)
  streak = db.Column(db.Integer, default=0, nullable=False)
  complete = db.Column(db.Boolean, default=False)

  user = db.relationship('User', back_populates='goals')
  subgoals = db.relationship('Subgoal', back_populates='goal', cascade='all, delete')

  def to_dict(self):
    return {
      "id": self.id,
      "user_id": self.user_id,
      "category": self.category,
      "title": self.title,
      "description": self.description,
      "meetline": self.meetline,
      "is_daily": self.is_daily,
      "streak": self.streak,
      "complete": self.complete
    }

class Subgoal(db.Model):
  __tablename__ = "subgoals"

  id = db.Column(db.Integer, primary_key=True)
  goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'))
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text)
  meetline = db.Column(db.Date, default=None)
  is_daily = db.Column(db.Boolean, default=False, nullable=False)
  streak = db.Column(db.Integer, default=0)
  complete = db.Column(db.Boolean, default=False)

  goal = db.relationship('Goal', back_populates="subgoals")

  def to_dict(self):
    return {
      "id": self.id,
      "goal_id": self.goal_id,
      "title": self.title,
      "description": self.description,
      "meetline": self.meetline,
      "is_daily": self.is_daily,
      "streak": self.streak,
      "complete": self.complete
    }

class Minigoal(db.Model):
  __tablename__ = "minigoals"

  id = db.Column(db.Integer, primary_key=True)
  objective = db.Column(db.String)

  def to_dict(self):
    return {
      "id": self.id,
      "objective": self.objective,
    }
