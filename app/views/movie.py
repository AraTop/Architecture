from flask import request
from flask_restx import Resource, Namespace
from app.dao.model.Movie import MovieSchema
from implemented import movie_service 

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):
   def get(self):
      all_movie = movie_service.get_all()
      return movies_schema.dump(all_movie), 200

   def post(self):
      req_json = request.json
      movie_service.create(req_json)
      return "", 201

@movie_ns.route('/int:<uid>')
class MovieView(Resource):

   def get(self,uid):
      movie = movie_service.get_one(uid)
      return  movie_schema.dump(movie)

   def put(self, uid):
      req_json = request.json
      req_json["id"] = uid

      movie_service.update(req_json)
      return "", 204
