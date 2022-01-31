from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError, Schema, fields
from werkzeug.exceptions import BadRequest

from dao.model.user import UserSchema
from exceptions import DuplicateError
from implemented import user_service
from tools.auth import auth_required
from views.auth import LoginValidator

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    # def get(self):
    #     rs = user_service.get_all()
    #     res = UserSchema(many=True).dump(rs)
    #     return res, 200

    def post(self):
        try:
            user_service.create(**LoginValidator().load(request.json))
        except ValidationError:
            raise BadRequest
        except DuplicateError:
            raise BadRequest('Username already exists')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self, token_data):
        return UserSchema().dump(user_service.get_one(token_data['user_id'])), 200
