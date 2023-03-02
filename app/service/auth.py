import calendar
import datetime
from flask import abort
from app.constants import JWT_SECRET , JWT_ALGORITHM
from app.service.user import UserService
import jwt

class AuthService:
   def __init__(self, user_service: UserService):
      """создание user_service для того чтоб его испольовать для получение пользователя при создание токена"""

      self.user_service = user_service

   def generate_tokens(self, user_name, password, is_refresh=False):
      """праверка подлиности пороля, именни , создание токеноф"""

      user = self.user_service.get_by_user_name(user_name)

      if user is None:
         raise abort(401)
      
      if not is_refresh:
         if not self.user_service.compare_passwords(user.password , password):
            abort(401)

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
      """получение refresh токена и return generate_tokens"""

      data = jwt.decode(JWT=refresh_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
      username = data.get("username")
      print(data, username)

      return self.generate_tokens(username, None , is_refresh=True)