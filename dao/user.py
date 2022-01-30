from dao.model.user import User
from exceptions import IncorrectData


class UserDAO:
    def __init__(self, session):
        self.session = session
        self._roles = {'user', 'admin'}

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_by_username(self, username: str):
        return self.session.query(User).filter(username=username).one_or_none()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update_role(self, username: str, role: str):
        if role not in self._roles:
            raise IncorrectData
        user = self.get_by_username(username)
        user.role = role
        self.session.add(user)
        self.session.commit()

    def update_password(self, username: str, password_hash: str):
        user = self.get_by_username(username)
        user.password = password_hash
        self.session.add(user)
        self.session.commit()

    def update(self, user):
        self.session.add(user)
        self.session.commit()
        return user
