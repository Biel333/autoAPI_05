from helpers.api_helper import request
from decouple import config


class TokenHelper:
    @staticmethod
    def get_token(client_credentials):
        body = {
            'grant_type': client_credentials,
            'client_id': config('CLIENT_ID'),
            'client_secret': config('CLIENT_SECRET'),
        }
        return request(
            method='POST',
            route='/api/v2/oauth/token',
            data=body
        )

    @staticmethod
    def update_token():
        body = {
            'grant_type': "refresh_token",
            'refresh_token': config('REFRESH_TOKEN_NOT_AUTH'),

        }
        return request(
            method='POST',
            route='/api/v2/oauth/token',
            data=body
        )

    def get_update_access_token(self):
        self.response = self.update_token()
        return self.response.json()["result"]["access_token"]

    def get_update_refresh_token(self):
        return self.response.json()["result"]["refresh_token"]

