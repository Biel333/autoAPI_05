import os

import pytest
from helpers.auth_helper import AuthHelper
from decouple import config


@pytest.fixture(autouse=True, scope="session")
def get_auth_token():
    response = AuthHelper.login(config("LOGIN"), config("PASSWORD"))
    os.environ["TOKEN"] = response.json()["result"]["access_token"]
