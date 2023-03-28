"""
This class models the redirect page of the weather shopper page
URL: sunscreen
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Sunscreen_page(Base_Page):
    "Page Object for the tutorial's redirect page"

    #locators
    # heading = locators.heading

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'sunscreen'
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading)
        self.conditional_write(result_flag,
            positive='Correct heading present on redirect page',
            negative='Heading on redirect page is INCORRECT!!',
            level='debug')

        return result_flag
