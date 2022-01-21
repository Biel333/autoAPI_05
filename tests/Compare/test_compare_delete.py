from helpers.compare_helper import CompareHelper
import json


class TestAddProductCompare:
    def setup_class(self):
        self.responce_delete = CompareHelper.delete_compare()
        self.responce_delete_product = CompareHelper.delete_product("619045")
        self.responce_delete_section = CompareHelper.delete_section("706", "59")
        products = ["619098", "601520"]
        self.responce_delete_products = CompareHelper.delete_products(products)

    # удалить товар из сравнения (один товар) #ЕСЛИ ТОВАР УЖЕ БЫЛ УДАЛЁН ВЫПАДЕТ ОШИБКА!
    def test_delete_product(self):
        assert self.responce_delete_product.status_code == 200
        print(json.dumps(
            self.responce_delete_product.json(),
            indent=5
        ))

    # удалить товары из сравнения (номера товаров через запятую)
    def test_delete_products(self):
        assert self.responce_delete_products.status_code == 200
        print(json.dumps(
            self.responce_delete_products.json(),
            indent=5
        ))

    # удалить раздел в сравнении
    def test_delete_section(self):
        assert self.responce_delete_section.status_code == 200
        print(json.dumps(
            self.responce_delete_section.json(),
            indent=5
        ))

    # очистить сравнение
    def test_delete_compare(self):
        assert self.responce_delete.status_code == 200
        print(json.dumps(
            self.responce_delete.json(),
            indent=5
        ))
