"""
========
Footer
========
"""
from tailored.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'Return Center': 'link=Return Center',
    'Return an item': 'link=Return an item',
    'Gift Wrapping': 'link=Gift Wrapping',
    'Forget Me': 'link=Forget Me',
    'eGift cards': 'link=eGift cards',
    'Store finder': 'link=Store finder',
    'Layaway': 'link=Layaway',
    'All departments': 'link=All departments',
    'Privacy policy': 'link=Privacy policy',
    'Terms of Use': 'link=Terms of Use',
    'Facebook fan page': 'link=Facebook fan page',
    'Twitter fan page': 'link=Twitter fan page',
    'Trending now': 'css=div.footerLinkCategoryContent ' \
        'a:nth-child(1) span.tmaSubline',
    'Toyland': 'css=div.footerLinkCategoryContent ' \
        'a:nth-child(2) span.tmaSubline'
}


class Footer(Page):
    """
    PO for the Footer section
    """
    def __init__(self, driver):
        self.locators = locators
        self.driver = driver
        self.config = cfg_wrapper().config
