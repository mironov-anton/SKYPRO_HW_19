from calendar import timegm
from datetime import datetime, timedelta
from typing import Dict, Any

import jwt
from flask import current_app
from marshmallow import Schema, fields


class JwtSchema(Schema):
    user_id = fields.Int(required=True)
    role = fields.Str(required=True)


class JwtToken:
    def __init__(self, data: Dict[str, Any]):
        self._now = datetime.now()
        self._data = data
        self._access_token_expiration = 10  # minutes
        self._refresh_token_expiration = 30  # days

    def _get_token(self, time_delta: timedelta) -> str:
        self._data.update({
            "exp": timegm((self._now + time_delta).timetuple())
        })
        return jwt.encode(self._data, current_app.config['SECRET_HERE'], algorithm="HS256")

    @property
    def _refresh_token(self) -> str:
        return self._get_token(time_delta=timedelta(days=self._refresh_token_expiration))

    @property
    def _access_token(self) -> str:
        return self._get_token(time_delta=timedelta(minutes=self._access_token_expiration))

    def get_tokens(self) -> Dict[str, str]:
        return {
            "access_token": self._access_token,
            "refresh_token": self._refresh_token,
        }

    @staticmethod
    def decode_token(token: str) -> Dict[str, Any]:
        return jwt.decode(token, current_app.config['SECRET_HERE'], algorithms="HS256")
