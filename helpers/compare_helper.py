from helpers.api_helper import request
from decouple import config


class CompareHelper:
    @staticmethod
    def add_product(productId): #добавить товар в сравнение
        return request(
            method='PUT',
            rout=f'/api/v1/compare/{productId}?show_entity=',
            authorization=True
        )

    @staticmethod
    def delete_compare(): #очистить сравнение
        return request(
            method='DELETE',
            rout='/api/v1/compare',
            authorization=True
        )