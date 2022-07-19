import datetime

from flask import jsonify
from flask_restful import reqparse, Resource, abort
from werkzeug.security import generate_password_hash

from data import db_sessions
from data.users import User
from request_parser import parser


def abort_if_user_not_found(id):
    sess = db_sessions.create_session()
    news = sess.query(User).get(id)
    if not news:
        abort(404, message=f'User {id} not found')


class UserResource(Resource):
    def get(self, id):
        abort_if_user_not_found(id)
        sess = db_sessions.create_session()
        user = sess.query(User).get(id)
        return jsonify({'user': user.to_dict(only=('id', 'name', 'age', 'position', 'speciality'))})

    def delete(self, id):
        abort_if_user_not_found(id)
        sess = db_sessions.create_session()
        user = sess.query(User).get(id)
        sess.delete(user)
        sess.commit()
        return jsonify({'success': 'ok'})


class UserListResource(Resource):
    def get(self):
        sess = db_sessions.create_session()
        users = sess.query(User).all()
        return jsonify(
            {'users': [item.to_dict(only=('id', 'name', 'age', 'position', 'speciality')) for item in users]})

    def post(self):
        args = parser.parse_args()
        sess = db_sessions.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=generate_password_hash(args['password']),
            modified_date=datetime.datetime.now()
        )
        sess.add(user)
        sess.commit()
        return jsonify({'success': 'ok'})
