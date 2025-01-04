from app.models import db, Goal, Subgoal, Minigoal
from datetime import date

# Demo Goals on Demo User
def seed_goals():
  demo_goal = Goal(
    user_id=1,
    category="Work",
    title="GET the goals",
    description="Produce this goal on the app frontend",
    meetline=None,
    is_daily=False,
    streak=0,
  )

  demo_subgoal = Subgoal(
    goal_id=1,
    title="GET the subgoals",
    description="Produce this subgoal on the app frontend",
    meet_by=None,
    is_daily=False,
    streak=None,
  )

  demo_minigoal = Minigoal(
    user_id=1,
    objective="Drink water",
    complete=False
  )

  db.session.add(demo_goal)
  db.session.add(demo_subgoal)
  db.session.add(demo_minigoal)
  db.session.commit()

def undo_goals():
  db.session.execute('TRUNCATE goals RESTART IDENTITY CASCADE;')
  db.session.execute('TRUNCATE subgoals RESTART IDENTITY CASCADE;')
  db.session.execute('TRUNCATE minigoals RESTART IDENTITY CASCADE;')
  db.session.commit()
