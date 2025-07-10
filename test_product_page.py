import pytest
from pages.product_page import ShellCodersPage
import time

@pytest.mark.negative
class TestProductPagePositive:
    """Тесты для проверки основной функциональности страницы продукта"""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        self.page = ShellCodersPage(browser, link)
        self.page.open()

    def test_add_to_basket(self):
        """Тест добавления товара в корзину и проверки промо-урла"""
        self.page.should_be_promo_url()
        self.page.add_to_basket()
        self.page.solve_quiz_and_get_code()

    def test_basket_price(self):
        """Тест сравнения цены товара на странице и в корзине"""
        self.page.add_to_basket()
        self.page.solve_quiz_and_get_code()
        self.page.should_be_same_price_in_basket()

    def test_basket_name(self):
        """Тест сравнения названия товара на странице и в корзине"""
        self.page.add_to_basket()
        self.page.solve_quiz_and_get_code()
        self.page.should_be_same_name()

@pytest.mark.negative
class TestProductPageWithOffers:
    """Тесты для проверки различных промо-предложений"""

    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                     marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ShellCodersPage(browser, link)
        page.open()
        page.should_be_promo_url()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_same_price_in_basket()
        page.should_be_same_name()

@pytest.mark.positive
class TestProductPageNegative:
    """Негативные тесты для страницы продукта"""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = ShellCodersPage(browser, link)
        self.page.open()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.page.add_to_basket()
        self.page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self):
        self.page.add_to_basket()
        self.page.should_not_disappeared_after_adding_product_to_basket()