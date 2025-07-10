import pytest
from pages.product_page import ShellCodersPage
import time

@pytest.fixture(scope="function")
def product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ShellCodersPage(browser, link)
    page.open()
    return page


def test_add_to_basket(product_page):
    """Тест добавления товара в корзину и проверки промо-урла"""
    product_page.should_be_promo_url()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

def test_basket_price(product_page):
    """Тест сравнения цены товара на странице и в корзине"""
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_same_price_in_basket()


def test_basket_name(product_page):
    """Тест сравнения названия товара на странице и в корзине"""
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_same_name()
    

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    page = ShellCodersPage(browser, link)
    page.open()
    page.should_be_promo_url()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_same_price_in_basket()
    page.should_be_same_name()