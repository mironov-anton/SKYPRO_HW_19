from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service
from tools.auth import auth_required

user_ns = Namespace('users')


# @user_ns.route('/')
# class UsersView(Resource):
#     def get(self):
#         rs = user_service.get_all()
#         res = UserSchema(many=True).dump(rs)
#         return res, 200


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self, token_data):
        return UserSchema().dump(user_service.get_one(token_data['user_id'])), 200
