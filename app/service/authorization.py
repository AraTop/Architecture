from app.service.auth import AuthService
from app.service.user import UserService


auth_service = AuthService(UserService)