from saunter.testcase.webdriver import SaunterTestCase

from pages.homepage import HomePage
from pages.header import Header
from pages.footer import Footer

import pytest
import random
import string


class TestMain(SaunterTestCase):
    @pytest.marks('shallow')
    def test_images_present(self):
        h = HomePage(self.driver)
        h.open_default_url()
        assert(h.is_element_available(h.locators['specials btn']))
        assert(h.is_element_available(h.locators['list textbox']))
        assert(h.is_element_available(h.locators['list btn']))

    @pytest.marks('shallow')
    def test_slide_nav(self):
        h = HomePage(self.driver)
        h.open_default_url()
        assert(h.is_slide_visible('slide 1'))
        h.go_to_next_slide()
        assert(h.is_slide_visible('slide 2'))
        h.go_to_next_slide()
        assert(h.is_slide_visible('slide 3'))
        h.go_to_prev_slide()
        assert(h.is_slide_visible('slide 2'))
        h.go_to_prev_slide()
        assert(h.is_slide_visible('slide 1'))

    @pytest.marks('shallow')
    def test_list_creation(self):
        name = ''.join(random.choice(
            string.ascii_lowercase + string.digits) for x in range(15))
        h = HomePage(self.driver)
        h.open_default_url()
        assert(h.create_list(name))
        self.driver.find_element_by_link_text('Find gifts now').click()
        assert(self.driver.current_url.endswith('/shops'))


class TestHeader(SaunterTestCase):
    @pytest.marks('shallow')
    def test_elements_present(self):
        HomePage(self.driver).open_default_url()
        h = Header(self.driver)
        for locator in h.locators:
            assert(h.is_element_available(h.locators[locator]))


class TestFooter(SaunterTestCase):
    @pytest.marks('shallow')
    def test_elements_present(self):
        HomePage(self.driver).open_default_url()
        f = Footer(self.driver)
        for locator in f.locators:
            assert(f.is_element_available(f.locators[locator]))
