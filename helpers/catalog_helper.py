from helpers.api_helper import request
import random


class CatalogHelper:
    # получаем все разделы каталога
    @staticmethod
    def get_sections_of_catalog(auth=False):
        return request(method="GET", rout="/api/v1/catalog/sections", authorization=auth)

    # выбираем один случайный раздел
    def get_random_section(self, auth=False):
        response = self.get_sections_of_catalog(auth=auth)
        body = response.json()
        ids = []
        for i in body["result"]:
            ids.append(i["ID"])

        return random.choice(ids)

    # получаем все товары из одного раздела
    @staticmethod
    def get_items_from_section(params, auth=False):
        return request(method="GET", route="/api/v1/snippets/vue/catalog", authorization=auth, params=params)

    def get_list_products_id_of_section(self, section_id, auth=False):
        response = self.get_items_from_section({
            "section_id": section_id,
        }, auth=auth)
        body = response.json()
        list_products_id = []
        for i in body["result"]["PRODUCTS_BLOCK"]["ITEMS"]:
            list_products_id.append(i["ID"])

        return list_products_id

    # получаем айди товаров с бесплатной доставкой (т.е. цена меньше 998 руб.)
    def get_product_id_free_delivery(self, section_id, auth=False):
        responce = self.get_items_from_section({
            "section_id": section_id,
        }, auth=auth)
        body = responce.json()
        products_id = []
        for i in body["result"]["PRODUCTS_BLOCK"]["ITEMS"]:
            if "PRICE" in i:
                if i["PRICE"] < 998:
                    products_id.append(i["ID"])
        return products_id

    # получаем айди товаров с платной доставкой (т.е. цена больше 1001 руб.)
    def get_product_id_not_free_delivery(self, section_id, auth=False):
        responce = self.get_items_from_section({
            "section_id": section_id,
        }, auth=auth)
        body = responce.json()
        products_id = []
        for i in body["result"]["PRODUCTS_BLOCK"]["ITEMS"]:
            if "PRICE" in i:
                if i["PRICE"] < 998:
                    products_id.append(i["ID"])
        return products_id

    @staticmethod
    def get_main_screen_vue(auth=False):
        return request(method="GET", route="/api/v1/snippets/vue/main", authorization=auth)

    @staticmethod
    def get_main_screen_mobile(auth=False):
        return request(method="GET", route="/api/v1/snippets/main", authorization=auth)

