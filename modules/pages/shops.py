"""
========
Shops
========
"""
from tailored.page import Page
from saunter.po.webdriver.text import Text
from saunter.po import string_timeout, timeout_seconds
from saunter.exceptions import ElementVisiblityTimeout
import time
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'collection list': 'css=ul.collectionsList li.collection',
    'collection image': 'css=div.collectionImage img',
    'collection title': 'css=li.collection:nth-of-type(N) h3'
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

    def get_collection_image_locations(self):
        return self.driver.find_elements_by_locator(
            locators['collection images'])

    def get_collection_name(self, index):
        return self.driver.find_element_by_locator(
            locators['collection title'].replace('N', str(index))).text

    def get_collections(self):
        return self.driver.find_elements_by_locator(
            locators['collection list'])

    def open_collection_by_name(self, index):
        self.driver.find_element_by_locator(
            locators['collection title'].replace('N', str(index))).click()
        #self.driver.find_element_by_link()

    def collection_page_title(self):
        return self.driver.find_element_by_locator(locators['collection name'])

    def collection_exists(self, url):
        self.driver.get(url)
        img = self.driver.find_element_by_locator('css=img')
        if 'error' not in img.get_attribute('alt'):
            return True
        else:
            return False
