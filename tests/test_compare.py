import pytest

from helpers.compare_helper import CompareHelper
from lib.assertions import Assertions
from decouple import config
import random
import json


# ДОБАВЛЕНИЕ В СРАВНЕНИЕ
class TestCompareAdd:
    auths = [
        ("True"), # с авторизацией
        ("False") # без авторизации
    ]

    def setup_class(self):
        # создаём список товаров и выбираем из него один случайный
        list_products_id = json.loads(config("PRODUCTS_ID_OF_PHONES"))
        self.product_id = random.choice(list_products_id)

    @pytest.mark.parametrize('auth', auths)
    def test_status_code_is_200(self, auth):
        # добавление товара  в сравнение и получение списка товаров в сравнении
        compare_helper = CompareHelper()
        self.response_add = compare_helper.add_product(self.product_id, auth=auth)
        self.response_get_all_products = compare_helper.get_all_products(auth=auth)
        # тест статус кода
        Assertions.assert_status_code(self.response_add, 200)
        # тест добавился ли нужный товар в сравнение
        assert self.response_get_all_products.json()["result"]["ITEMS"][0]["ID"] == self.product_id
        CompareHelper.delete_compare(auth=auth)
    #
    # def test_correct_id(self):
    #

    # @pytest.mark.parametrize('auth', auths)
    # # очищение сравнения
    # def teardown_class(self, auth):
    #     CompareHelper.delete_compare(auth=auth)


# УДАЛЕНИЕ ИЗ СРАВНЕНИЯ
class TestDeleteCompare:
    def setup_class(self):
        # compare_helper = CompareHelper()
        # response = compare_helper.get_list_products_id_of_compare(auth=True)
        # v = json.dumps(response)
        # self.list_of_ids = v

        # создаём список товаров и выбираем из него один случайный
        list_products_id = json.loads(config("PRODUCTS_ID_OF_PHONES"))
        self.product_id = random.choice(list_products_id)
        self.product_id2 = random.choice(list_products_id)

        # добавление 2 товара в сравнение
        self.response_add = CompareHelper.add_product(self.product_id, auth=True)
        self.response_add2 = CompareHelper.add_product(self.product_id2, auth=True)

        # удаление 1 товара из сравнения
        self.response_delete_product = CompareHelper.delete_product(self.product_id, auth=True)

        # получение списка товаров в сравнении
        self.response_get_all_products = CompareHelper.get_all_products(auth=True)

        # удаление нескольких товаров из сравнения
        products = [random.choice(list_products_id), random.choice(list_products_id)]
        self.response_delete_products = CompareHelper.delete_products(products, auth=True)

        # удалить раздел
        self.response_delete_section = CompareHelper.delete_section("706", "59", auth=True)

        # очистить сравнение
        self.response_delete = CompareHelper.delete_compare(auth=True)

    # удалить товар из сравнения (один товар) ЕСЛИ ТОВАР УЖЕ БЫЛ УДАЛЁН ВЫПАДЕТ ОШИБКА!
    def test_delete_product(self):
        Assertions.assert_status_code(self.response_delete_product, 200)

        body = self.response_get_all_products.json()
        list_products_id = []
        for i in body["result"]["ITEMS"]:
            list_products_id.append(i["ID"])
        # assert self.response_delete_product.status_code == 200
        print(list_products_id)
        assert self.product_id not in list_products_id

    # удалить товары из сравнения (номера товаров через запятую)
    def test_delete_products(self):
        Assertions.assert_status_code(self.response_delete_products, 200)

    # удалить раздел в сравнении
    def test_delete_section(self):
        Assertions.assert_status_code(self.response_delete_section, 200)

    # очистить сравнение
    def test_delete_compare(self):
        Assertions.assert_status_code(self.response_delete, 200)


# ПОЛУЧИТЬ СРАВНЕНИЕ
class TestCompareGet:
    def setup_class(self):
        self.response_get_section = CompareHelper.get_section(auth=True)
        self.response_get_section_list = CompareHelper.get_section_list(auth=True)
        self.response_get_all_products = CompareHelper.get_all_products(auth=True)

    # получить структуру сравнения
    def test_get_section(self):
        Assertions.assert_status_code(self.response_get_section, 200)

    # получить список разделов в сравнении
    def test_get_section_list(self):
        Assertions.assert_status_code(self.response_get_section_list, 200)

    # получить все товары сравнения
    def test_get_all_products(self):
        Assertions.assert_status_code(self.response_get_all_products, 200)

    # очищение сравнения
    def teardown_class(self):
        CompareHelper.delete_compare()
