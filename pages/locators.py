from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_T0_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_OF_GOODS = (By.CSS_SELECTOR, ".product_main p")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    SUCCESS_FORM = (By.CSS_SELECTOR, ".alertinner strong")
    NAME_OF_GOODS = (By.CSS_SELECTOR, ".product_main h1")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR,".btn-group a")
    BASKET_INFO = (By.CSS_SELECTOR, ".content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "[type='email']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "[type='password']")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR,'[name="registration-email"]')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTER_PASSWORD_AGAIN_INPUT = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR,'[name="registration_submit"]')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


