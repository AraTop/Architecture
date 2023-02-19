from app.dao.Director import DirectorDAO
from app.dao.Genre import GenreDAO
from app.service.director import DirectorService
from app.service.genre import GenreService
from app.setup_db import db
from app.dao.Movie import MovieDAO
from app.service.movie import MovieService


movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)