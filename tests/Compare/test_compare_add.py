from helpers.compare_helper import CompareHelper


class TestCompareAdd:
    def setup_class(self):
        #ID товаров: 619098, 619045
        self.responce_add = CompareHelper.add_product("619098")

    # добавить товар в сравнение
    def test_add_product(self):
        assert self.responce_add.status_code == 200
