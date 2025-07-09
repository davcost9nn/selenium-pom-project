import pytest
from pages.product_page import ShellCodersPage

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