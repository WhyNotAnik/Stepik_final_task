from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    MESSAGE_THIS_PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, ".alertinner > strong:nth-child(1)")
    MESSAGE_OF_CART_PRICE_EQUAL_TO_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
