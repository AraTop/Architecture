from flask import request
from flask_restx import Resource, Namespace
from implemented import auth_service

auth_ns = Namespace('auth')

@auth_ns.route("/")
class AuthsView(Resource):
   def post(self):
      data = request.json
      if data:
         try:
            username = data.get("username")
            password = data.get("password")
         
            if None in [username , password]:
               return "", 400

            tokens = auth_service.generate_tokens(username, password)
         except Exception as s:
            return str(s), 404

      return tokens, 201

   def put(self):
      data = request.json
      if data:
         try:
            token = data.get("refresh_token")
            tokens = auth_service.refresh_token(token)
            return tokens, 201
         except Exception as s:
            return str(s)