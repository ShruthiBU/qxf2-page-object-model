"""
This class models the main Selenium tutorial page.
URL: selenium-tutorial-main
The page consists of a header, footer, form and table objects
"""

from .Base_Page import Base_Page
from .sunscreen_page_object import Sunscreen_page_object
from .moisturizer_page_object import Moisturizer_page_object
from .cart_page_object import Cart_object
from .iframe_object import Iframe_objects
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Weather_Main_Page(Base_Page,Sunscreen_page_object,Moisturizer_page_object,
                            Cart_object,Iframe_objects):
    "Page Object for the tutorial's main page"


    #locators
    degree_temperature = locators.temperature
    product_sunscreen = locators.sunscreen
    product_moisturizer = locators.moisturizer
    confirmation = locators.confirmation

    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/'
        self.open(url)


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def get_temperature(self):
        "get the temperature from the website"
        
        temperature_element = self.get_element(self.degree_temperature)
        temperature_value = temperature_element.text.strip().split()[0]

        return temperature_value
    

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_product(self, temperature_value):

        if int(temperature_value) > 30:
            result_flag = self.click_sunscreen()
        else:
            result_flag = self.click_moisturizer()

        self.conditional_write(result_flag,
            positive='Successfully clicked on the Buy product button',
            negative='Failed to click on the Buy product button',
            level='debug')
        
        return result_flag


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_sunscreen(self):
        "Click on 'Sunscreen' button"
        result_flag = self.click_element(self.product_sunscreen)
        self.conditional_write(result_flag,
            positive='Clicked on the "Sunscreen" button',
            negative='Failed to click on "click me" button',
            level='debug')

        return result_flag
    

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_moisturizer(self):
        "Click on 'Moisturizer' button"
        result_flag = self.click_element(self.product_moisturizer)
        self.conditional_write(result_flag,
            positive='Clicked on the "Moisturizer" button',
            negative='Failed to click on "click me" button',
            level='debug')

        return result_flag
    