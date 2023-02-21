from app.dao.model.Movie import Movie

class MovieDAO:
   def __init__(self, session):
      self.session = session

   def get_all(self):
      return self.session.query(Movie).all()
   
   def create(self, data):
      movie = Movie(**data)

      self.session.add(movie)
      self.session.commit()

      return movie

   def get_one(self, mid):
      return self.session.query(Movie).get(mid)

   def update(self, data):
      self.session.add(data)
      self.session.commit()

   def delete(self, mid):
      movie = self.get_one(mid)

      self.session.delete(movie)
      self.session.commit()

   def get_director_id(self, mid):
      return self.session.query(Movie).filter(Movie.director_id == mid).first()

   def get_genre_id(self, mid):
      return self.session.query(Movie).filter(Movie.genre_id == mid).first()

   def get_year(self, mid):
      return self.session.query(Movie).filter(Movie.year == mid).first()