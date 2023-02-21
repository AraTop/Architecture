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
   
   #def get(self):
      director_id = request.args.get("director_id")
      movie = movie_service.get_director_id(director_id)
      return movie_schema.dump(movie)

   #def get(self):
      genre_id = request.args.get("genre_id")
      movie = movie_service.get_genre_id(genre_id)
      return movie_schema.dump(movie)

   #def get(self):
      year = request.args.get("year")
      movie = movie_service.get_year(year)
      return movie_schema.dump(movie)

@movie_ns.route('/<int:uid>')
class MovieView(Resource):

   def get(self,uid):
      movie = movie_service.get_one(uid)
      return movie_schema.dump(movie)

   def put(self, uid):
      req_json = request.json
      req_json["id"] = uid

      movie_service.update(req_json)
      return "", 204

   def delete(self, uid):
      return movie_service.delete(uid)

@movie_ns.route('')
class Movie(Resource):
   def get(self):

      if request.args.get("director_id"):
         director_id = request.args.get("director_id")
         movie = movie_service.get_director_id(director_id)
         return movie_schema.dump(movie)

      elif request.args.get("genre_id"):
         genre_id = request.args.get("genre_id")
         movie = movie_service.get_genre_id(genre_id)
         return movie_schema.dump(movie)

      elif request.args.get("year"):
         year = request.args.get("year")
         movie = movie_service.get_year(year)
         return movie_schema.dump(movie)

      else:
         return "лох"