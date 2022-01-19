from helpers.api_helper import request
from helpers.compare_helper import CompareHelper


class TestAddProductCompare:
    def setup_class(self):
        self.responce_add = CompareHelper.add_product("619051")
        self.responce_delete = CompareHelper.delete_compare()

    def test_delete_comare(self):
        assert self.responce_delete.status_code == 200

    def test_add_product(self):
        assert self.responce_add.status_code == 200

