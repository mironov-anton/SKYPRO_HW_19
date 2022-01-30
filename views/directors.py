from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from tools.auth import auth_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self, token_data):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid, token_data):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
