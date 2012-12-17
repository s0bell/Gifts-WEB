from saunter.testcase.webdriver import SaunterTestCase

from pages.products import Products
from pages.header import Header
from pages.footer import Footer

import pytest


class TestMain(SaunterTestCase):
    @pytest.marks('shallow')
    def test_filters(self):
        p = Products(self.driver)
        p.open_default_url()

        # Test Product Filter visibility when scrolling
        p.scroll_to_end_of_page()
        assert(p.is_product_filter_visible())

        # I'm shopping for
        assert(p.get_field_value('person') == 'someone')
        p.set_field_value('person', 'him')
        assert(p.get_field_value('person') == 'him')

        # Who is
        assert(p.get_field_value('age') == 'any age')
        p.set_field_value('age', 'an adult (26+)')
        assert(p.get_field_value('age') == 'an adult (26+)')

        # And likes
        assert(p.get_field_value('likes') == 'everything')
        p.set_field_value('likes', 'home')
        assert(p.get_field_value('likes') == 'home')

        # Sort by
        p.sort_by('price low to high')
        prices = p.get_all_prices()
        cur_price = sorted(prices, reverse=False)[0]
        for price in prices:
            assert(price >= cur_price)
            cur_price = price

        p.sort_by('price high to low')
        prices = p.get_all_prices()
        cur_price = sorted(prices, reverse=True)[0]
        for price in prices:
            assert(price <= cur_price)
            cur_price = price

        # Price range
        for i in (25, 50, 100, 150):
            p.sort_by_price('under $%s' % i)
            prices = p.get_all_prices()
            cur_price = sorted(prices, reverse=True)[0]
            for price in prices:
                assert(price <= cur_price)
                cur_price = price

        # Reset filters
        p.click_reset()
        assert(p.get_field_value('person') == 'someone')
        assert(p.get_field_value('age') == 'any age')
        assert(p.get_field_value('likes') == 'everything')


class TestHeader(SaunterTestCase):
    @pytest.marks('shallow')
    def test_elements_present(self):
        Products(self.driver).open_default_url()
        h = Header(self.driver)
        for locator in h.locators:
            assert(h.is_element_available(h.locators[locator]))


class TestFooter(SaunterTestCase):
    @pytest.marks('shallow')
    def test_elements_present(self):
        Products(self.driver).open_default_url()
        f = Footer(self.driver)
        for locator in f.locators:
            assert(f.is_element_available(f.locators[locator]))
