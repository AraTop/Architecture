from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.user import UserSchema
from app.helpers.decorators import auth_required
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        all_movies = user_service.get_all()
        users_schema = UserSchema(many=True).dump(all_movies)
        return users_schema, 200

    def post(self):
        req_json = request.json
        movie = user_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@user_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required
    def get(self, bid):
        user = user_service.get_one(bid)
        user_schema = UserSchema().dump(user)
        return user_schema, 200

    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        user_service.update(req_json)
        return "", 204

    def delete(self, bid):
        user_service.delete(bid)
        return "", 204
