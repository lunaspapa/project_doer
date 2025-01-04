from flask import Blueprint, request, jsonify
from app.models import db, Goal, Subgoal, Minigoal

goal_routes = Blueprint("goals")

@goal_routes.route('/<user_id>')
def get_goals(user_id):
  query = Goal.query.filter_by(user_id=user_id).all()
  goals = [goal.to_dict() for goal in query]
  return { "goals": goals }

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
