import hmac
from app.constants import PWD_ITERATIONS , PWD_SALT
from app.dao.user import UserDAO
import hashlib
import base64

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data["password"] = self.generate_password(user_data["password"])
        return self.dao.create(user_data)

    def update(self, user_data):
        user_data["password"] = self.generate_password(user_data["password"])
        return self.dao.update(user_data)

    def delete(self, uid):
        self.dao.delete(uid)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            PWD_SALT,
            PWD_ITERATIONS

        )
        return base64.b64encode(hash_digest)

    def get_by_user_name(self, user_name):
        return self.dao.get_by_user_name(user_name)

    def compare_passwords(self, password_hash , other_password):
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            other_password.encode("utf-8"),
            PWD_SALT,
            PWD_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)