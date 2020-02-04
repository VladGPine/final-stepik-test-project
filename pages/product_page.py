from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_to_basket(self):
        self.should_be_product_page()
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_page(self):
        assert ProductPageLocators.PRODUCT_PATH in self.browser.current_url, \
            'this is not a product page'

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            'add to basket button is not presented'

    def should_be_message_about_adding_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDING_MESSAGE), \
            'no such element(product name) on the page'

    def should_be_product_name_in_adding_product_to_basket_message_equal_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message_about_adding_product_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDING_MESSAGE)
        assert message_about_adding_product_to_basket.text == product_name.text, \
            'product name in message not equal product name'

    def should_be_message_about_price_adding_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_ADDING_MESSAGE), \
            'no such element(price) on the page'

    def should_be_product_price_equal_in_basket_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        assert product_price.text in product_price_in_basket.text, \
            'prices not equal'
