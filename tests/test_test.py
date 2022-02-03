import json

import requests
from decouple import config


class BaseTestClass:

    def __init__(self):
        self.auth = True

    def request(self, method, route, **kwargs):
        url = config('BASE_URL') + route
        if self.auth:
            token = config('ACCESS_TOKEN_AUTH')
            if "headers" in kwargs:
                kwargs["headers"] = kwargs["headers"] | {"Authorization": F"Bearer {token}"}
            else:
                kwargs["headers"] = {"Authorization": F"Bearer {token}"}
        else:
            token1 = config('ACCESS_TOKEN_NOT_AUTH')
            if "headers" in kwargs:
                kwargs["headers"] = kwargs["headers"] | {"Authorization": F"Bearer {token1}"}
            else:
                kwargs["headers"] = {"Authorization": F"Bearer {token1}"}

        return requests.request(method=method, url=url, **kwargs)


class TestCompareAdd2(BaseTestClass):

    def test_add_product(self):

        response_add = self.request(
            method='PUT',
            route=f'/api/v1/compare/{601520}?show_entity='
        )

        response_get_all_products = self.request(
            method='GET',
            route='/api/v1/compare/products'
        )

        assert response_add.status_code == 200 and \
               response_get_all_products.json()["result"]["ITEMS"][0]["ID"] == "601520"


    def teardown(self):
        self.request(
            method='DELETE',
            route='/api/v1/compare',
        )
