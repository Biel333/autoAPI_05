from helpers.compare_helper import CompareHelper


class TestCompareGet:
    def setup_class(self):
        self.responce_get_section = CompareHelper.get_section()
        self.responce_get_section_list = CompareHelper.get_section_list()
        self.responce_get_all_products = CompareHelper.get_all_products()

    # получить структуру сравнения
    def test_get_section(self):
        assert self.responce_get_section.status_code == 200

    # получить список разделов в сравнении
    def test_get_section_list(self):
        assert self.responce_get_section_list.status_code == 200

    # получить все товары сравнения
    def test_get_all_products(self):
        assert self.responce_get_all_products.status_code == 200
