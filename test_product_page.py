from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    timeout = 10
    page = ProductPage(browser, link, timeout)
    page.browser.implicitly_wait(timeout)
    page.open()
    #time.sleep(5)
    page.add_product_to_cart()
    #time.sleep(1)
    page.solve_quiz_and_get_code()
    page.should_be_message_product_added()
    page.should_be_message_cart_price()
    time.sleep(5)