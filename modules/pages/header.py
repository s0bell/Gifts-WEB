"""
========
Header
========
"""
from tailored.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'Shop walmart.com': 'css=div.backToDotCom',
    'Walmart gifts logo': 'id=logo',
    'Main logo': 'css=#bannerCenterLogo.navLink img',
    'My cart': 'id=myCartIcon',
    'Login': 'id=loginIcon',
    'Find gifts': 'id=findGiftsButton',
    'Gift lists': 'link=Gift lists',
    'Search box': 'id=friendsAndInterestsSearch',
    'Trending now': 'css=#mainNav.group div.holidayNav a:nth-child(1)',
    'Toyland': 'css=#mainNav.group div.holidayNav a:nth-child(2)'
}


class Header(Page):
    """
    PO for the Header section
    """
    def __init__(self, driver):
        self.locators = locators
        self.driver = driver
        self.config = cfg_wrapper().config
