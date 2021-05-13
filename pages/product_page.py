from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def should_be_message_product_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_product_added = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADDED)
        assert product_name.text == message_product_added.text,\
            "The item added to the cart is different from the intended"

    # cart price should be equal to product price
    def should_be_message_cart_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message_cart_price = self.browser.find_element(*ProductPageLocators.MESSAGE_CART_PRICE)
        assert product_price.text == message_cart_price.text,\
            "The price of the cart is not equal to product's price"