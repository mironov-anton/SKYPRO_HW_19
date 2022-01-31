from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest, abort

from dao.model.user import UserSchema
from exceptions import DuplicateError
from implemented import user_service
from tools.auth import auth_required, admin_required
from views.auth import LoginValidator

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def post(self):
        try:
            user_service.create(**LoginValidator().load(request.json))
        except ValidationError:
            raise BadRequest
        except DuplicateError:
            raise BadRequest('Username already exists')

# """for debug"""
    # def get(self):
    #     ud = user_service.get_all()
    #     res = UserSchema(many=True).dump(ud)
    #     return res, 200

@user_ns.route('/<int:uid>')
class UserView(Resource):
    @auth_required
    def get(self, token_data):
        return UserSchema().dump(user_service.get_one(token_data['user_id'])), 200

    @admin_required
    def patch(self, token_data):
        req_json = request.json
        if "username" not in req_json:
            return "", 400
        if "role" in req_json:
            user_service.update_role(req_json["username"], req_json["role"])
        if "password" in req_json:
            user_service.update_password(req_json["username"], req_json["password"])
        return "", 204
