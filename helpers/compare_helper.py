from helpers.api_helper import request


class CompareHelper:
    # добавить товар в сравнение
    @staticmethod
    def add_product(productId, auth=False):
        return request(
            method='PUT',
            route=f'/api/v1/compare/{productId}?show_entity=',
            authorization=auth)

    @staticmethod
    def get_all_products_compare(auth=False):
        return request(
            method='GET',
            route='/api/v1/compare/products',
            authorization=auth)

    # получить id товаров сравнения
    # def get_list_products_id_of_compare(self, auth=False):
    #     response = self.get_all_products_compare(auth=auth)
    #     body = response.json()
    #     list_products_id = []
    #     for i in body["result"]["ITEMS"]:
    #         list_products_id.append(i["ID"])
    #
    #     return list_products_id

    # получить структуру сравнения
    @staticmethod
    def get_section(auth=False):
        return request(
            method='GET',
            route='/api/v1/compare',
            authorization=auth)

    # получить список разделов в сравнении
    @staticmethod
    def get_section_list(auth=False):
        return request(
            method='GET',
            route='/api/v1/compare/sections',
            authorization=auth)

    # получить все товары из сравнения
    @staticmethod
    def get_all_products(auth=False):
        return request(
        method='GET',
        route='/api/v1/compare/products',
        authorization=auth)

    # удалить раздел
    @staticmethod
    def delete_section(sectionId, iblockId, auth=False):
        return request(
            method='DELETE',
            route=f'/api/v1/compare/section/{sectionId}/{iblockId}',
            authorization=auth)

    # удалить товары (несколько товаров)
    @staticmethod
    def delete_products(products, auth=False):

        return request(
            method='DELETE',
            route=f'/api/v1/compare/products/{",".join(products)}',
            authorization=auth)

    # удалить товар из сравнения (один товар)
    @staticmethod
    def delete_product(productId, auth=False):
        return request(
            method='DELETE',
            route=f'/api/v1/compare/{productId}?show_entity=',
            authorization=auth)

    # очистить сравнение
    @staticmethod
    def delete_compare(auth=False):
        return request(
            method='DELETE',
            route='/api/v1/compare',
            authorization=auth)
