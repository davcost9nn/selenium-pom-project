from typing import assert_type

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ShellCodersLocators


class ShellCodersPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ShellCodersLocators.ADD_T0_BASKET)
        link.click()


    def should_be_promo_url(self):
        assert "?promo=newYear" in self.browser.current_url, "Promo URL is not correct "

    def should_be_same_price_in_basket(self):
        price_on_page = self.browser.find_element(*ShellCodersLocators.PRICE_OF_GOODS).text
        price_in_basket = self.browser.find_element(*ShellCodersLocators.PRICE_IN_BASKET).text
        price_on_page_num = float(''.join(c for c in price_on_page if c.isdigit() or c == '.'))
        price_in_basket_num = float(''.join(c for c in price_in_basket if c.isdigit() or c == '.'))
        assert price_on_page_num == price_in_basket_num, \
            f"Prices are different: {price_on_page} (page) vs {price_in_basket} (basket)"

    def should_be_same_name(self):
        name_on_page = self.browser.find_element(*ShellCodersLocators.NAME_OF_GOODS).text
        name_in_basket = self.browser.find_element(*ShellCodersLocators.SUCCESS_FORM).text
        assert name_on_page == name_in_basket[0:len(name_on_page)], \
            f"Names are different: {name_on_page} (page) vs {name_in_basket} (basket)"