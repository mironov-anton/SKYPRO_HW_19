from marshmallow import fields, Schema

from setup_db import db


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	role = db.Column(db.String)

class UserSchema(Schema):
	id = fields.Int()
	username = fields.Str()
	password = fields.Str(load_only=True)
	role = fields.Str()
