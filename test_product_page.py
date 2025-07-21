import pytest
from pages.product_page import ShellCodersPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

@pytest.mark.product_test
class TestProductPagePositive:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        self.page = ShellCodersPage(browser, link)
        self.page.open()

    def test_add_to_basket(self):
        self.page.should_be_promo_url()
        self.page.add_to_basket()
        self.page.solve_quiz_and_get_code()

    def test_basket_price(self):
        self.page.add_to_basket()
        self.page.solve_quiz_and_get_code()
        self.page.should_be_same_price_in_basket()

    def test_basket_name(self):
        self.page.add_to_basket()
        self.page.solve_quiz_and_get_code()
        self.page.should_be_same_name()

@pytest.mark.product_with_offers_test
class TestProductPageWithOffers:

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

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ShellCodersPage(browser, link)
        page.open()
        page.should_be_promo_url()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_same_price_in_basket()
        page.should_be_same_name()

@pytest.mark.negative_tests
class TestProductPageNegative:

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

@pytest.mark.login_from_any_page
class TestAnyPageLogin:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = ShellCodersPage(browser, link)
        self.page.open()

    def test_guest_should_see_login_link_on_product_page(self):
        self.page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page (self):
        self.page.go_to_login_page()
        self.page.should_be_same_address('https://selenium1py.pythonanywhere.com/ru/accounts/login/')

@pytest.mark.basket_test
class TestBasket:

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = BasketPage(browser, link)
        self.page.open()
        self.page.go_to_basket()
        self.page.should_be_empty_basket()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = BasketPage(browser, link)
        self.page.open()
        self.page.go_to_basket()
        self.page.should_be_empty_basket()

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # 1. Сначала регистрируем пользователя через LoginPage
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.register_new_user(email=str(time.time()) + "@fakemail.org", password="Qwerty1234)")
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self,browser):
        product_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = ShellCodersPage(browser, product_link)
        self.page.open()
        self.page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self,browser):
        product_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = ShellCodersPage(browser, product_link)
        self.page.open()
        self.page.add_to_basket()
        self.page.should_be_same_price_in_basket()
        self.page.should_be_same_name()
