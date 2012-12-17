from saunter.po.webdriver.page import Page as SaunterPage
from saunter.po import timeout_seconds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


class Page(SaunterPage):
    def wait_for_jquery_active(self):
        w = WebDriverWait(self.driver, self.config.getint(
            "Selenium", "timeout"))
        w.until(lambda driver: driver.execute_script(
            "return jQuery.active === 0"))
