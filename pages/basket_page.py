from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS) , "Basket is not empty"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_INFO).text == 'Ваша корзина пуста' ,"No message about empty basket"
