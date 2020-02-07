from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_present_any_products(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_BASKET), \
            'Basket has items, but should not'

    def should_be_product_item(self):
        assert self.is_element_present(*BasePageLocators.PRODUCT_IN_BASKET), \
            'Basket is empty'

    def should_present_empty_basket_message(self):
        assert self.browser.find_element(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            'Empty basket message is not presented on the page'

    def should_not_present_empty_basket_message(self):
        assert self.is_not_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            'Empty basket message is presented on the page, but should not'
