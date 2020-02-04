from pages.product_page import ProductPage
import time

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.adding_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.should_be_message_about_adding_product_to_basket()
    page.should_be_product_name_in_adding_product_to_basket_message_equal_product_name()
    page.should_be_message_about_price_adding_product_to_basket()
    page.should_be_product_price_equal_in_basket_product_price()
