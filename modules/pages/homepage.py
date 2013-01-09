"""
========
HomePage
========
"""
from tailored.page import Page
from saunter.po.webdriver.text import Text
from saunter.po import string_timeout, timeout_seconds
from saunter.exceptions import ElementVisiblityTimeout
import time
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'list textbox': 'css=input.nameYourList',
     'list btn': 'css=form.createNewListContent input.button:nth-child(3)',
     'specials btn': 'css=img.homeAdvert',
     'prev slide': 'id=headlineArrowLeft',
     'next slide': 'id=headlineArrowRight',
     'slide 1': 'id=headlineSlide1',
     'slide 2': 'id=headlineSlide2',
     'slide 3': 'id=headlineSlide3'
}


class HomePage(Page):
    """
    PO for the Home page
    """
    def __init__(self, driver):
        self.locators = locators
        self.driver = driver
        self.config = cfg_wrapper().config

    def open_default_url(self):
        self.driver.get(self.config.get('Selenium', 'base_url'))

    def go_to_next_slide(self):
        self.driver.find_element_by_locator(locators['next slide']).click()

    def go_to_prev_slide(self):
        self.driver.find_element_by_locator(locators['prev slide']).click()

    def is_slide_visible(self, slide):
        time.sleep(1)
        if self.wait_for_visible(locators[slide]):
            return True
        return False

    def create_list(self, name):
        box = self.driver.find_element_by_locator(locators['list textbox'])
        box.send_keys(name)
        box.submit()
        if self.wait_for_text('css=div.centerText h1', 'Your list has been created'):
            return True
        return False
