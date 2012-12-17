"""
========
Products
========
"""
from tailored.page import Page
from saunter.po.webdriver.text import Text
from saunter.po import string_timeout, timeout_seconds
from saunter.exceptions import ElementVisiblityTimeout
import time
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'product filter box': 'css=#productFilterWrapper-sticky-wrapper',
    'person': 'css=#filterPerson span.ui-selectmenu-status',
    'age': 'css=#filterAge span.ui-selectmenu-status',
    'likes': 'css=#filterCategory span.ui-selectmenu-status',
    'product prices': 'css=li.product div.productInner a.productModalTrigger',
    'price': {
        'under $25': 'link=Under $25',
        'under $50': 'link=Under $50',
        'under $100': 'link=Under $100',
        'under $150': 'link=Under $150',
        'any': 'link=Any Price'
    },
    'price low to high': 'link=Price (Low to High)',
    'price high to low': 'link=Price (High to Low)',
    'reset': 'css=#filterCategory img.filterResetButton'
}


class Products(Page):
    """
    PO for the Products page
    """
    def __init__(self, driver):
        self.locators = locators
        self.driver = driver
        self.config = cfg_wrapper().config

    def open_default_url(self):
        self.driver.get(self.config.get("Selenium", "base_url") + "/products")

    def click_reset(self):
        self.driver.find_element_by_locator(locators['reset']).click()
        self.wait_for_jquery_active()

    def set_field_value(self, loc, val):
        self.wait_for_jquery_active()
        self.driver.find_element_by_locator(locators[loc]).click()
        self.driver.find_element_by_xpath("//a[text()='%s']" % val).click()

    def get_field_value(self, loc):
        return self.driver.find_element_by_locator(locators[loc]).text

    def sort_by_price(self, loc):
        self.wait_for_jquery_active()
        self.driver.find_element_by_locator(locators['price'][loc]).click()

    def sort_by(self, loc):
        self.wait_for_jquery_active()
        self.driver.find_element_by_locator(locators[loc]).click()

    def get_all_prices(self):
        prices = self.driver.find_elements_by_locator(locators['product prices'])
        return [float(i.text.lstrip('$')) for i in prices]

    def is_product_filter_visible(self):
        self.wait_for_jquery_active()
        filters_box = self.driver.find_element_by_locator(
            locators['product filter box'])
        return filters_box.is_displayed()

    def scroll_to_end_of_page(self):
        self.wait_for_jquery_active()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
