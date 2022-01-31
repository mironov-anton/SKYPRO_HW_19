from flask import request, abort
from flask_restx import Resource, Namespace

# from dao.model.genre import GenreSchema
from exceptions import DuplicateError
from implemented import user_service
# from tools.auth import auth_required
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import BadRequest

from tools.jwt_token import JwtSchema, JwtToken
from tools.security import compare_passwords

auth_ns = Namespace('auth')


class LoginValidator(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class RefreshTokenValidator(Schema):
    refresh_token = fields.Str(required=True)


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        """Create tokens"""
        try:
            validated_data = LoginValidator().load(request.json)
            user = user_service.get_by_username(validated_data['username'])
            if not user:
                abort(401)

            if not compare_passwords(user.password, validated_data['password']):
                abort(401)

            token_data = JwtSchema().load({'user_id': user.id, 'role': user.role})
            return JwtToken(token_data).get_tokens(), 201

        except ValidationError:
            abort(400)

    def put(self):
        """Update token"""
        try:
            validated_data = RefreshTokenValidator().load(request.json)
            token_data = JwtToken.decode_token(validated_data)
            user = user_service.get_one(token_data['user_id'])
            if not user:
                abort(401)

            new_token_data = JwtSchema().load({'user_id': user.id, 'role': user.role})
            return JwtToken(new_token_data).get_tokens(), 201

        except ValidationError:
            abort(400)
