import pytest
from helpers.auth_helper import AuthHelper
from helpers.token_helper import TokenHelper
from helpers.catalog_helper import CatalogHelper
from decouple import config
import json
import os


@pytest.fixture(autouse=True, scope="session")
def get_auth_token():
    try:
        response = AuthHelper.login(config("LOGIN"), config("PASSWORD"))
        os.environ["ACCESS_TOKEN_AUTH"] = response.json()["result"]["access_token"]
        os.environ["REFRESH_TOKEN_AUTH"] = response.json()["result"]["refresh_token"]
    except KeyError:
        raise Exception("Не получилось авторизоваться")
        pass


@pytest.fixture(autouse=True, scope="session")
def get_not_auth_token():
    try:
        response = TokenHelper.get_token("client_credentials")
        os.environ["ACCESS_TOKEN_NOT_AUTH"] = response.json()["result"]["access_token"]
        os.environ["REFRESH_TOKEN_NOT_AUTH"] = response.json()["result"]["refresh_token"]
    except KeyError:
        raise Exception("Не получилось получить токен")
        pass


@pytest.fixture(autouse=True, scope="session")
def get_products_id_from_phones():
    try:
        catalog_helper = CatalogHelper()
        response = catalog_helper.get_list_products_id_of_section("705")
        os.environ["PRODUCTS_ID_OF_PHONES"] = json.dumps(response)
    except KeyError:
        raise Exception("Секции каталога 705 нет")
        pass


@pytest.fixture(autouse=True, scope="session")
def get_products_id_free_delivery():
    try:
        catalog_helper = CatalogHelper()
        response = catalog_helper.get_product_id_free_delivery("5586")
        os.environ["PRODUCTS_ID_FREE_DELIVERY"] = json.dumps(response)
    except KeyError:
        raise Exception("Секции каталога 5586 нет")
        pass


@pytest.fixture(autouse=True, scope="session")
def get_products_id_not_free_delivery():
    try:
        catalog_helper = CatalogHelper()
        response = catalog_helper.get_product_id_not_free_delivery("5586")
        os.environ["PRODUCTS_ID_NOT_FREE_DELIVERY"] = json.dumps(response)
    except KeyError:
        raise Exception("Секции каталога 5586 нет")
        pass




