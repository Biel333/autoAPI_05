from helpers.compare_helper import CompareHelper
import json


# ДОБАВЛЕНИЕ В СРАВНЕНИЕ
class TestCompareAdd:
    def setup_class(self):
        # добавление товаров  в сравнение
        self.response_add = CompareHelper.add_product("601520", auth=True)
        CompareHelper.add_product("619098", auth=True)

        self.response_get_all_products = CompareHelper.get_all_products(auth=True)

    # тест добавить товар в сравнение
    def test_add_product(self):
        assert self.response_add.status_code == 200 and \
               self.response_get_all_products.json()["result"]["ITEMS"][0]["ID"] == "601520"

        print(json.dumps(
            self.response_get_all_products.json(),
            indent=5
        ))

    # очищение сравнения
    def teardown_class(self):
        CompareHelper.delete_compare()


# УДАЛЕНИЕ ИЗ СРАВНЕНИЯ
class TestDeleteCompare:
    def setup_class(self):
        CompareHelper.add_product("619098")
        CompareHelper.add_product("619045")
        CompareHelper.add_product("601520")

        self.response_delete_product = CompareHelper.delete_product("601520")
        products = ["619098", "619045"]
        self.response_delete_products = CompareHelper.delete_products(products)
        self.response_delete_section = CompareHelper.delete_section("706", "59")
        self.response_delete = CompareHelper.delete_compare()

    # удалить товар из сравнения (один товар) #ЕСЛИ ТОВАР УЖЕ БЫЛ УДАЛЁН ВЫПАДЕТ ОШИБКА!
    def test_delete_product(self):
        assert self.response_delete_product.status_code == 200
        print(json.dumps(
            CompareHelper.get_all_products().json(),
            indent=5
        ))

    # удалить товары из сравнения (номера товаров через запятую)
    def test_delete_products(self):
        assert self.response_delete_products.status_code == 200
        print(json.dumps(
            CompareHelper.get_all_products().json(),
            indent=5
        ))

    # удалить раздел в сравнении
    def test_delete_section(self):
        assert self.response_delete_section.status_code == 200
        print(json.dumps(
            CompareHelper.get_all_products().json(),
            indent=5
        ))

    # очистить сравнение
    def test_delete_compare(self):
        assert self.response_delete.status_code == 200
        print(json.dumps(
            CompareHelper.get_all_products().json(),
            indent=5
        ))


# ПОЛУЧИТЬ СРАВНЕНИЕ
class TestCompareGet:
    def setup_class(self):
        CompareHelper.add_product("619098")
        CompareHelper.add_product("619045")
        CompareHelper.add_product("601520")

        self.responce_get_section = CompareHelper.get_section()
        self.responce_get_section_list = CompareHelper.get_section_list()
        self.responce_get_all_products = CompareHelper.get_all_products()

    # получить структуру сравнения
    def test_get_section(self):
        assert self.responce_get_section.status_code == 200
        print(json.dumps(
            self.responce_get_section.json(),
            indent=5
        ))

    # получить список разделов в сравнении
    def test_get_section_list(self):
        assert self.responce_get_section_list.status_code == 200
        print(json.dumps(
            self.responce_get_section_list.json(),
            indent=5
        ))

    # получить все товары сравнения
    def test_get_all_products(self):
        assert self.responce_get_all_products.status_code == 200
        print(json.dumps(
            self.responce_get_all_products.json(),
            indent=5
        ))

    # очищение сравнения
    def teardown_class(self):
        CompareHelper.delete_compare()
