from dao.user import UserDAO
from tools.security import get_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, username: str):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, username, password, role: str = "user"):
        self.dao.create({
            "username": username,
            "password": get_password_hash(password),
            "role": role,
        })

    def update_password(self, username: str, password_hash: str):
        return self.dao.update_password(username, password_hash)

    def update_role(self, username: str, role: str):
        return self.dao.update_role(username, role)

    def delete(self, uid):
        self.dao.delete(uid)
