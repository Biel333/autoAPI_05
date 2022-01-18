import requests
from helpers.api_helper import request
from decouple import config


class TestDeliveryAddress:
    def setup_class(self):
        self.responce = request(
            method='GET',
            rout='/api/v1/darkstore/delivery-areas',
            authorization=True,
            headers={"X_SHOP_ID":"DARKSTORE"})

    def test_get(self):
        assert self.responce.status_code == 200
