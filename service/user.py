from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        return self.dao.create(user_d)

    def update_password(self, username: str, password_hash: str):
        return self.dao.update_password(username, password_hash)

    def update_role(self, username: str, role: str):
        return self.dao.update_role(username, role)

    def delete(self, uid):
        self.dao.delete(uid)
