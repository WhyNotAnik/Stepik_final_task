from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def should_be_message_this_product_added_to_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_this_product_added_to_cart = self.browser.find_element(*ProductPageLocators.MESSAGE_THIS_PRODUCT_ADDED_TO_CART).text
        assert product_name == message_this_product_added_to_cart, "The item added to the cart is different from the intended"

    def should_be_message_of_cart_price_equal_to_product_prise(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_of_cart_price_equal_to_product_price = self.browser.find_element(*ProductPageLocators.MESSAGE_OF_CART_PRICE_EQUAL_TO_PRODUCT_PRICE).text
        assert product_price == message_of_cart_price_equal_to_product_price, "The price of the cart is not equal to product's price"