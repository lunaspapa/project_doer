from flask import Blueprint, request, jsonify
from app.models import db, Postie

postie_routes = Blueprint("postie")

# POSTIE
# Retrieve a user's posties
@postie_routes.route('/<user_id>')
def get_posties(user_id):
  query = Postie.query.filter_by(user_id=user_id).all()
  posties = [postie.to_dict() for postie in query]
  return { 'posties': posties }

# Create a Postie
@postie_routes.route('/new')
def post_postie():
  data = request.json
  if data:
    postie = Postie(
      user_id=data['user_id'],
      note=data['note']
    )
    db.session.add(postie)
    db.session.commit()
    return postie.to_dict()

# Update the note
@postie_routes.route('/<postie_id>/update')
def update_postie(postie_id):
  postie = Postie.query.get(postie_id)
  data = request.json
  if data:
    postie.note=data['note']
    db.session.commit()
    return postie.to_dict()

@postie_routes.route('/<postie_id>/delete')
def delete_postie(postie_id):
  postie = Postie.query.get(postie_id)
  db.session.delete(postie)
  db.session.commit()
  return postie.to_dict()
