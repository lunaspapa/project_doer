from flask import Blueprint, request, jsonify
from app.models import db, Goal, Subgoal, Minigoal

goal_routes = Blueprint("goals")

# Retrieve a user's goals
@goal_routes.route('/<user_id>')
def get_goals(user_id):
  query = Goal.query.filter_by(user_id=user_id).all()
  goals = [goal.to_dict() for goal in query]
  return { "goals": goals }

# Create a goal
@goal_routes.route('/new', methods=['POST'])
def post_goal():
  data = request.json()
  if data:
    goal = Goal(
      user_id=data['user_id'],
      category=data['category'],
      title=data['title'],
      description=data['description'],
      meetline=data['meetline'],
      is_daily=data['is_daily'],
    )
    db.session.add(goal)
    db.session.commit()
    return goal.to_dict()

# Update general goal contents
@goal_routes.route('/<goal_id>/update', methods=['PUT'])
def update_goal(goal_id):
  goal = Goal.query.get(goal_id)
  data = request.json
  if data:
    goal.title = data['title']
    goal.description = data['description']
    goal.is_daily = data['is_daily']
    goal.meetline = data['meetline']
    db.session.commit()
    return goal.to_dict()

# Tick up the goal completion streak
@goal_routes.route('/<goal_id>/update/streak', methods=['PUT'])
def uptick_streak(goal_id):
  goal = Goal.query.get(goal_id)
  goal.streak = goal.streak + 1
  db.session.commit()
  return goal.to_dict()

# Update goal when complete
@goal_routes.route('/<goal_id>/update/complete', methods=['PUT'])
def complete_goal(goal_id):
  goal = Goal.query.get(goal_id)
  goal.complete = True
  db.session.commit()
  return goal.to_dict()

# Mark goal as incomplete
@goal_routes.route('/<goal_id>/update/uncomplete', methods=['PUT'])
def uncomplete_goal(goal_id):
  goal = Goal.query.get(goal_id)
  goal.complete = False
  db.session.commit()
  return goal.to_dict()

# Delete a goal
@goal_routes.route('/<goal_id>/delete', methods=['DELETE'])
def delete_goal(goal_id):
  goal = Goal.query.get(goal_id)
  db.session.delete(goal)
  db.session.commit()
  return goal.to_dict()
