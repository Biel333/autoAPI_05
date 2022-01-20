from helpers.api_helper import request
from helpers.compare_helper import CompareHelper
import json


class TestAddProductCompare:
    def setup_class(self):
        self.responce_delete = CompareHelper.delete_compare()
        self.responce_add = CompareHelper.add_product("619098")
        self.responce_add2 = CompareHelper.add_product("619045")
        self.responce_delete_product = CompareHelper.delete_product("619045")
        self.responce_get_section = CompareHelper.get_section()
        self.responce_get_section_list = CompareHelper.get_section_list()
        self.responce_get_all_products = CompareHelper.get_all_products()
        print(json.dumps(
            self.responce_get_all_products.json(),
            indent=5
        ))

        self.responce_delete_section = CompareHelper.delete_section("706", "59")
        products = ["619098", "619045"]
        self.responce_delete_products = CompareHelper.delete_products(products)


    # очистить сравнение
    def test_delete_compare(self):
        assert self.responce_delete.status_code == 200

    # добавить товар в сравнение
    def test_add_product(self):
        assert self.responce_add.status_code == 200

    # удалить товар из сравнения (один товар)
    def test_delete_product(self):
        assert self.responce_delete_product.status_code == 200

    # получить структуру сравнения
    def test_get_section(self):
        assert self.responce_get_section.status_code == 200

    # получить список разделов в сравнении
    def test_get_section_list(self):
        assert self.responce_get_section_list.status_code == 200

    # получить все товары сравнения
    def test_get_all_products(self):
        assert self.responce_get_all_products.status_code == 200

    # удалить раздел в сравнении
    def test_delete_section(self):
        assert self.responce_delete_section.status_code == 200

    # удалить товары из сравнения (номера товаров через запятую)
    def test_delete_products(self):
        assert self.responce_delete_products.status_code == 200

