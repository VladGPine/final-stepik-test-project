from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            'add to basket button is not presented'

    def should_be_message_about_adding_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDING_MESSAGE), \
            'no such element(product name) on the page'

    def return_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def return_message_about_adding_product_to_basket(self):
        message_about_adding_product_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDING_MESSAGE)
        return message_about_adding_product_to_basket.text

    @staticmethod
    def should_be_product_name_in_adding_product_to_basket_message_equal_product_name(
            product_name,
            product_name_in_message):
        assert product_name_in_message == product_name, \
            'product name in message not equal product name'

    def should_be_message_about_price_adding_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_ADDING_MESSAGE), \
            'no such element(price) on the page'

    def return_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def return_product_price_in_basket(self):
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        return product_price_in_basket.text

    @staticmethod
    def should_be_product_price_equal_in_basket_product_price(product_price, product_price_in_basket):
        assert product_price in product_price_in_basket, \
            'prices not equal'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDING_MESSAGE), \
            'adding product message is presented, but should not'

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDING_MESSAGE), \
            'adding product message still presented on the page, but should not'
