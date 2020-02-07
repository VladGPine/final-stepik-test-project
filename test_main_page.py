from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = 'http://selenium1py.pythonanywhere.com/'


# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_present_any_products()
    basket_page.should_present_empty_basket_message()
