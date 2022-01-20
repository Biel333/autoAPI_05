from helpers.api_helper import request
from decouple import config


class CompareHelper:
    # добавить товар в сравнение
    @staticmethod
    def add_product(productId):
        return request(
            method='PUT',
            rout=f'/api/v1/compare/{productId}?show_entity=',
            authorization=True)

    # очистить сравнение
    @staticmethod
    def delete_compare():
        return request(
            method='DELETE',
            rout='/api/v1/compare',
            authorization=True)

    # удалить товар из сравнения (один товар)
    @staticmethod
    def delete_product(productId):
        return request(
            method='DELETE',
            rout=f'/api/v1/compare/{productId}?show_entity=',
            authorization=True)

    # получить структуру сравнения
    @staticmethod
    def get_section():
        return request(
            method='GET',
            rout='/api/v1/compare',
            authorization=True)

    # получить список разделов в сравнении
    @staticmethod
    def get_section_list():
        return request(
        method='GET',
        rout='/api/v1/compare/sections',
        authorization=True)

    @staticmethod
    def get_all_products():
        return request(
        method='GET',
        rout='/api/v1/compare/products',
        authorization=True)

    @staticmethod
    def delete_section(sectionId, iblockId):
        return request(
            method='DELETE',
            rout=f'/api/v1/compare/section/{sectionId}/{iblockId}',
            authorization=True)

    @staticmethod
    def delete_products(products):

        return request(
            method='DELETE',
            rout=f'/api/v1/compare/products/{",".join(products)}',
            authorization=True)
