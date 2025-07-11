

from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators

class ShellCodersPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_T0_BASKET)
        link.click()

    def should_be_promo_url(self):
        assert "?promo=" in self.browser.current_url, "Promo URL is not correct "

    def should_be_same_price_in_basket(self):
        price_on_page = self.browser.find_element(*ProductPageLocators.PRICE_OF_GOODS).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        price_on_page_num = float(''.join(c for c in price_on_page if c.isdigit() or c == '.'))
        price_in_basket_num = float(''.join(c for c in price_in_basket if c.isdigit() or c == '.'))
        assert price_on_page_num == price_in_basket_num, \
            f"Prices are different: {price_on_page} (page) vs {price_in_basket} (basket)"

    def should_be_same_name(self):
        name_on_page = self.browser.find_element(*ProductPageLocators.NAME_OF_GOODS).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_FORM).text
        assert name_on_page == success_message, \
            f"Names are different: {name_on_page} (page) vs {success_message} (basket)"

    def should_be_same_address(self,link):
        assert self.is_same_address(link) , f"This is not {link}"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


# Negative tests
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_FORM), \
           "Success message is presented, but should not be"


    def should_not_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_FORM), \
            "Success message not disappeared, but should be"

