from flask_restx import Resource, Namespace
from app.dao.model.Director import DirectorSchema
from implemented import director_service 

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):
   def get(self):
      all_director = director_service.get_all()
      return directors_schema.dump(all_director), 200

@director_ns.route('/<int:uid>')
class DirectorsView(Resource):

   def get(self,uid):
      director = director_service.get_one(uid)
      return  director_schema.dump(director)