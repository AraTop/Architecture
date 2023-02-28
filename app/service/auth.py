import calendar
import datetime
from flask import abort
from app.constants import JWT_SECRET , JWT_ALGORITHM
from app.service.user import UserService
import jwt
from app.service.authorization import auth_service

class AuthService:
   def __init__(self, user_service: UserService):
      self.user_service = user_service

   def generate_tokens(self, user_name, password, is_refresh=False):
      user = auth_service.generate_token(user_name, password)
      print(user)

      if user in None:
         raise abort(404)
      
      if not is_refresh:
         if not self.user_service.compare_passwords(user.password , password):
            abort(400)

      data = {

         "username": user.username,
         "role": user.role

      }
      #создание на 30 мин access_token
      min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
      data["exp"] = calendar.timegm(min30.timetuple())
      access_token = jwt.encode(data , JWT_SECRET, algorithm=JWT_ALGORITHM)
      #создание на 130 дней refresh_token
      days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
      data["exp"] = calendar.timegm(days130.timetuple())
      refresh_token = jwt.encode(data , JWT_SECRET, algorithm=JWT_ALGORITHM)

      return {

         "access_token": access_token,
         "refresh_token": refresh_token
      }


   def refresh_token(self, refresh_token):
      data = jwt.decode(JWT=refresh_token, Key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
      username = data.get("username")

      return self.generate_tokens(username, None , is_refresh=True)