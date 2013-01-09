from saunter.testcase.webdriver import SaunterTestCase

from pages.shops import Shops
from pages.header import Header
from pages.footer import Footer

import pytest


class TestMain(SaunterTestCase):
    @pytest.marks('shallow')
    def test_shop_hyperlinks(self):
        s = Shops(self.driver)

        # Test title hyperlinks on first three shops
        for i in range(1, 3):
            s.open_default_url()
            shop = s.get_shop(i)
            title = s.get_shop_title(shop)
            s.open_shop_by_title(shop)
            assert(s.get_shop_title_from_current_page() == title)

        # Test thumbnail hyperlinks on first three shops
        for i in range(1, 3):
            s.open_default_url()
            shop = s.get_shop(i)
            title = s.get_shop_title(shop)
            s.open_shop_by_thumbnail(shop)
            assert(s.get_shop_title_from_current_page() == title)


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
