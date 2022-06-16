import requests
from helpers.auth_helper import AuthHelper
from decouple import config


class TestLogInPositive:
    def setup_class(self):
        self.response = AuthHelper.login(config("LOGIN"), config("PASSWORD"))

    def test_response_status_code_is_200(self):
        assert self.response.status_code == 200
