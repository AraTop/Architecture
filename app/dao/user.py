from app.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        ent = User(**user_data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        User = self.get_one(uid)
        self.session.delete(User)
        self.session.commit()

    def update(self, user_data):
        User = self.get_one(user_data.get("id"))
        
        if user_data.get("username"):
            User.username = user_data.get("username")
        if user_data.get("password"):
            User.password = user_data.get("password")
        if user_data.get("role"):
            User.role = user_data.get("role")

        self.session.add(User)
        self.session.commit()

    def get_by_user_name(self, user_name):
        return self.session.query(User).filter(User.username == user_name).one()