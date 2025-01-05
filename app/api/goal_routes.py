from flask import Blueprint, request, jsonify
from app.models import db, Goal, Subgoal, Minigoal

goal_routes = Blueprint("goals")

# GOAL
# Retrieve a user's goals
@goal_routes.route('/<user_id>')
def get_goals(user_id):
  query = Goal.query.filter_by(user_id=user_id).all()
  goals = [goal.to_dict() for goal in query]
  return { "goals": goals }

# Create a goal
@goal_routes.route('/new', methods=['POST'])
def post_goal():
  data = request.json
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

# Tick up the daily goal completion streak
@goal_routes.route('/<goal_id>/update/streak', methods=['PUT'])
def uptick_goal_streak(goal_id):
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

# SUBGOAL
# Retrieve subgoals on a goal
@goal_routes.route('/subgoals/<goal_id>')
def get_subgoals(goal_id):
  query = Subgoal.query.filter_by(goal_id=goal_id).all()
  if query:
    subgoals = [subgoal.to_dict() for subgoal in query]
    return {
      "subgoals": subgoals
    }

# Create a new subgoal
@goal_routes.route('/subgoals/new')
def new_subgoal():
  data = request.json
  if data:
    subgoal = Subgoal(
      goal_id=data['goal_id'],
      title=data['title'],
      description=data['description'],
      meetline=data['meetline'],
      is_daily=data['is_daily'],
    )
    db.session.add(subgoal)
    db.session.commit()
    return subgoal.to_dict()

# Update the contents of a subgoal
@goal_routes.route('/<subgoal_id>/update')
def update_subgoal(subgoal_id):
  data = request.json
  subgoal = Subgoal.query.get(subgoal_id)
  if data:
    subgoal.title=data['title']
    subgoal.description=data['description']
    subgoal.meetline=['meetline']
    subgoal.is_daily=['is_daily']
    db.session.commit()
    return subgoal.to_dict()

# Uptick the daily streak on a subgoal
@goal_routes.route('/<subgoal_id>/update/streak')
def uptick_subgoal_streak(subgoal_id):
  subgoal = Subgoal.query.get(subgoal_id)
  subgoal.streak = subgoal.streak + 1
  db.session.commit()
  return subgoal.to_dict()

# Mark a subgoal as complete
@goal_routes.route('/<subgoal_id>/update/complete')
def complete_subgoal(subgoal_id):
  subgoal = Subgoal.query.get(subgoal_id)
  subgoal.complete = True
  db.session.commit()
  return subgoal.to_dict()

# Mark a subgoal as uncomplete
@goal_routes.route('/<subgoal_id>/update/uncomplete')
def uncomplete_subgoal(subgoal_id):
  subgoal = Subgoal.query.get(subgoal_id)
  subgoal.complete = False
  db.session.commit()
  return subgoal.to_dict()

# Delete a subgoal
@goal_routes.route('/<subgoal_id>/delete')
def delete_subgoal(subgoal_id):
  subgoal = Subgoal.query.get(subgoal_id)
  db.session.delete(subgoal)
  db.session.commit()
  return subgoal.to_dict()

# MINIGOAL
# Users can't create minigoals
# A user receives 10 minigoals per day
# Minigoals are randomly generated, and a user can't receive two of the same in one day
# I will seed minigoals myself and dispense them randomly in a set of 10 to each user each day
# Most of the work will be done on the frontend
# Probably don't even need a table for them
