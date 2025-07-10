from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_T0_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_OF_GOODS = (By.CSS_SELECTOR, ".product_main p")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")
    SUCCESS_FORM = (By.CSS_SELECTOR, ".alertinner strong")
    NAME_OF_GOODS = (By.CSS_SELECTOR, ".product_main h1")