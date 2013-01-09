"""
========
Shops
========
"""
from tailored.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'shop': 'css=li.collection:nth-of-type(N)',
    'shop title': 'css=a.collectionLink h3.title',
    'shop thumbnail': 'css=a.collectionLink img',
    'page shop title': 'css=div.generalContainer h2.title',
}


class Shops(Page):
    """
    PO for the Shops page
    """
    def __init__(self, driver):
        self.locators = locators
        self.driver = driver
        self.config = cfg_wrapper().config

    def open_default_url(self):
        self.driver.get(self.config.get("Selenium", "base_url") + "/shops")

    def get_shop(self, index):
        return self.driver.find_element_by_locator(
            locators['shop'].replace('N', str(index)))

    def get_shop_title(self, shop):
        return shop.find_element_by_locator(
            locators['shop title']).text

    def get_shop_title_from_current_page(self):
        self.wait_for_jquery_active()
        return self.driver.find_element_by_locator(
            locators['page shop title']).text

    def open_shop_by_title(self, shop):
        shop.find_element_by_locator(
            locators['shop title']).click()

    def open_shop_by_thumbnail(self, shop):
        shop.find_element_by_locator(
            locators['shop thumbnail']).click()
