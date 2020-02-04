from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    PRODUCT_PATH = 'the-shellcoders-handbook_209'
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"].btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '.basket-mini')
    PRODUCT_ADDING_MESSAGE = (By.CSS_SELECTOR, '.alertinner > strong')
    PRODUCT_PRICE_ADDING_MESSAGE = (By.CSS_SELECTOR, '.alertinner > p > strong')