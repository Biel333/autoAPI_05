from helpers.compare_helper import CompareHelper
import json


class TestCompareAdd:
    def setup_class(self):
        #ID товаров: 619098, 619045, 623277, 601520
        self.responce_add = CompareHelper.add_product("601520")
        self.responce_get_all_products = CompareHelper.get_all_products()

    # добавить товар в сравнение
    def test_add_product(self):
        assert self.responce_add.status_code == 200

        print(json.dumps(
            self.responce_get_all_products.json(),
            indent=5
        ))
