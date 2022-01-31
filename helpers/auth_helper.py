from helpers.api_helper import request
from decouple import config


class AuthHelper:
    @staticmethod
    def login(username, password):
        body = {
            'grant_type': config('GRANT_TYPE'),
            'client_id': config('CLIENT_ID'),
            'client_secret': config('CLIENT_SECRET'),
            'username': username,
            'password': password
        }
        return request(
            method='POST',
            route='/api/v2/oauth/token',
            data=body
        )
