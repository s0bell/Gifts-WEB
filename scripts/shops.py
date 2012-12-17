from saunter.testcase.webdriver import SaunterTestCase

from pages.Shops import Shops
from pages.header import Header
from pages.footer import Footer

import pytest


class TestMain(SaunterTestCase):
    @pytest.marks('shallow')
    def test_something(self):
        s = Shops(self.driver)
        s.open_default_url()

        # Test links on first 10 collection names
        for i in range(1, 10):
            name = s.get_collection_name(i)
            s.open_collection_by_name(i)
            assert(s.current_collection_name == name)
            s.open_default_url()


class TestHeader(SaunterTestCase):
    @pytest.marks('shallow')
    def test_elements_present(self):
        Shops(self.driver).open_default_url()
        h = Header(self.driver)
        for locator in h.locators:
            assert(h.is_element_available(h.locators[locator]))


class TestFooter(SaunterTestCase):
    @pytest.marks('shallow')
    def test_elements_present(self):
        Shops(self.driver).open_default_url()
        f = Footer(self.driver)
        for locator in f.locators:
            assert(f.is_element_available(f.locators[locator]))
